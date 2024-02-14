# AI_Python_Progromming
Learn AI-Assisted Python Programming Book Code and Note  
https://learning.oreilly.com/library/view/learn-ai-assisted-python/9781633437784/  


How to run Code on Github CodeSpaces on this repo    
https://www.youtube.com/watch?v=kvJf8s18Vr4   

### -- See also my UpNote (Copilot Programming Book Note) --   

### To git commit all changes in the Codespaces:   
git add *  
git commit -m "update readme.md"  
git push    


### Use Codellama-70B to run copilot prompt inside the book  
prompt_used_in_book.txt  


### To run and debug python function in interactive mode at the terminal:  
type python in the terminal  
\>>> import function1  
\>>> function1.best_word(['zap', 'pack', 'quack'])   

Once you’ve imported a module for the first time, you won’t be able to import it again using another import statement. If you want to reload the module and run it once again, then you can use the reload() function, which forces the interpreter to import the module again:    

\>>> import hello  
Hello World!  

\>>> import importlib  
\>>> importlib.reload(hello)  
Hello World!  
  
How to import function reference:     
https://realpython.com/run-python-scripts/#using-the-python-command  
https://stackoverflow.com/questions/46996982/how-to-import-all-defined-functions-from-python-script-one-into-python-script-tw  
