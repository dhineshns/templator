# templator
CLI tool to generate text out of templates. 

# Edit template.txt file
Anything following ```<<<any text here>>>``` format, will be replaced with the text entered from the CLI prompt. 
## Example

Paste the follwing in template.txt
```
Hi <<<TO_NAME>>>, 
Please return the <<<BOOK_NAME>> book, that you borrowed on <<<DATE>>>.
Thank you so much <<<TO_NAME>>>.
-Dhinesh
```

and run the following command via Terminal.
> python main.py templator.txt

Follow the prompt and voila, you got your text generated. 
