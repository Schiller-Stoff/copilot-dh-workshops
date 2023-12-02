

# Development via copilot

Examples for small everyday operations that can be performed via copilot.


## CSS Selectors  

Task: There is a need to style every third li element in a list with the id #MY_LIST.The list elements should have a lightblue background and dashed border. The border color should be red.  

Solution(s):
    - use the "Github Copilot: Generate This" command via VSCode and prompt: I need a CSS statement selecting  every third li element of the list with id #MY_LIST. These li elements should have a lightblue background, a dashed border and the border color should be red. 
    - create a demo.css file and use copilot's autcompletions / suggestions feature: Provide additional context via comments and naming to solve the problem. 

```css

#MY_LIST li:nth-child(3n) {
    background-color: lightblue;
    border: 1px dashed red;
}

```

inside demo.css:

```css

/* select every third li element of the list with id #MY_LIST. */
#MY_LIST li:nth-child(3n) {
    /*apply lightblue background, dashed border with red border-color*/

}


```