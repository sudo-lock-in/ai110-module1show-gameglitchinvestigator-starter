# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

I put a winning input and it broke afterwards. Was not accepting any new input or starting a new game. I expected the game to basically refresh and begin a session but it was just stuck on telling me I won.
- List at least two concrete bugs you noticed at the start   (for example: "the secret number kept changing" or "the hints were backwards").

Top blue banner not accurately updating and difficulty logic being mismatched.


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 

Copilot with Claude and GPT. Both with Agent Mode and Ask Before Edit mode.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

I asked the AI to add logic that will restart the game when the difficulty is changed. It essientally repeated the same logic as new game but triggered when the difficulty is changed. I previewed the code and accepted it as I saw it made sense. Then I ran the app myself to make sure it worked and it did.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I was having issues with the debug menu not showing what I expect. For example, the history array and the attempt count shown did not match up with what was happening in the game. The AI proposed many different solutions which either raised new errors or did not change anything at all from when I tested the app. It was looking for the mistake in other parts of the code that would not have an affect on it. I realized I had to explain my issue in more detail and ended up with the solution of moving the debug menu code below all the logic so it updates with it properly (and also is in a better place in UI).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided a bug was fixed based on test cases made in Pytest and through exhausting a feature when I ran the app myself.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

I was manually testing if the enter key could consistently submit inputs. The first solution I came up with had bugs as it was too simplistic but after addressing it with Copilot the problem was finally solved.

- Did AI help you design or understand any tests? How?

The AI explained and assisted with the testing process including giving me the terminal commands to run the tests. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

The secret number kept changing at first due to poor tracking of when the game is being played, is lost, or is won. It should only be randomized again at when the new game is created.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns based on the initialized session states. It is not a typical page refresh.

- What change did you make that finally gave the game a stable secret number?

It was solved when I handled the game status with using session state. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

  - This could be a testing habit, a prompting strategy, or a way you used Git.

I think the way I went beyond just fixing bugs but also making the game more playable and generally more logical is very important. I ran it myself very often and did not just view the program as code. It is also an experience which needs to be taken into account as the UI end is what users will be dealing with. Adding exceptions for out of range to prevent wasted attempts for example made the game feel more polished. I also enjoyed using the AI to explain the code for me. It helped me get started in a codebase that was intiially unfamiliar.
- What is one thing you would do differently next time you work with AI on a coding task?

I would write more code without assistance first just to have a deeper understanding of the program.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

I realize that AI code can be very useful tool. It was quite satisfying and also extremely helpful in explaining things to me. I feel that I am learning more efficiently than if I did a project without it.
