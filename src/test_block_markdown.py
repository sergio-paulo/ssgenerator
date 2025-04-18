import unittest
from block_markdown import BlockType, markdown_to_blocks, block_to_block_type, extract_title

class TestUtilities(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
        
    def test_markdown_to_blocks_more_newlinew(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
""" 
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here"
            ])
    
    def test_markdown_to_blocks_no_newline(self):
        md = "This is **bolded** paragraph"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is **bolded** paragraph"])
    
    def test_markdown_to_blocks_with_whitespaces(self):
        md = """
    This is **bolded** paragraph

     This is another paragraph with _italic_ text and `code` here
""" 
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here"
            ])
        
    def test_block_to_block_type_heading(self):
        md = "# This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)
    
    def test_block_to_block_type_heading_3(self):
        md = "### This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)
        
    def test_block_to_block_type_heading_6(self):
        md = "###### This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)
        
    def test_block_to_block_type_code(self):
        md = "```\nThis is a code block\nwith multiline\n```"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_block_to_block_type_quote(self):
        md = ">This is the first line of a quote\n>This is the second line of a quote"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.QUOTE)
        
    def test_block_to_block_type_unordered_list(self):
        md = "- This is the first line of a list\n- This is the second line of a list"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.ULIST)
    
    def test_block_to_block_type_ordered_list(self):
        md = "1. This is the first line of a list\n2. This is the second line of a list\n3. This is the third line of a list"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.OLIST)
        
    def test_extract_title(self):
        md = ("# Hello")
        title = extract_title(md)
        self.assertEqual(title, "Hello")
        
    def test_extract_title_2(self):
        md = """
# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien

## Blog posts

- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)

## Reasons I like Tolkien

- You can spend years studying the legendarium and still not understand its depths
- It can be enjoyed by children and adults alike
- Disney _didn't ruin it_ (okay, but Amazon might have)
- It created an entirely new genre of fantasy

## My favorite characters (in order)

1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn

Here's what `elflang` looks like (the perfect coding language):

```
func main(){
    fmt.Println("Aiya, Ambar!")
}
```

Want to get in touch? [Contact me here](/contact).

This site was generated with a custom-built [static site generator](https://www.boot.dev/courses/build-static-site-generator-python) from the course on [Boot.dev](https://www.boot.dev).
"""
        title = extract_title(md)
        self.assertEqual(title, "Tolkien Fan Club")

    def test_extract_title_no_title(self):
        md = """
## Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien

## Blog posts

- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)

## Reasons I like Tolkien

- You can spend years studying the legendarium and still not understand its depths
- It can be enjoyed by children and adults alike
- Disney _didn't ruin it_ (okay, but Amazon might have)
- It created an entirely new genre of fantasy

## My favorite characters (in order)

1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn

Here's what `elflang` looks like (the perfect coding language):

```
func main(){
    fmt.Println("Aiya, Ambar!")
}
```

Want to get in touch? [Contact me here](/contact).

This site was generated with a custom-built [static site generator](https://www.boot.dev/courses/build-static-site-generator-python) from the course on [Boot.dev](https://www.boot.dev).
"""
        try:
            title = extract_title(md)
        except ValueError as e:
            self.assertEqual(str(e), "No title found in markdown file")
        
        
if __name__ == "__main__":
    unittest.main()