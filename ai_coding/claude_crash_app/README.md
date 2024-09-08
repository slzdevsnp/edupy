# Claude Crash Course Templates

Welcome to the **Claude Crash Course** repository! This repo contains three essential templates that will help you rapidly build and deploy AI-driven applications using Claude. These templates are part of a structured workflow designed to enhance your development process and help you code 10x faster.

## Overview

In this crash course, you will learn how to efficiently build AI applications by leveraging Claude's power. The templates provided here are designed to guide you through the entire development process, from generating a master plan for your project to fully implementing production-ready code.

### Templates Included:

1. **Generate Master Plan (`1_generate_master_plan.txt`)**:

   - This template helps you define the overall structure and purpose of your app. By answering key questions, you'll generate a `masterplan.md` file, which serves as a blueprint for the entire project.

2. **Stub Out Project (`2_stub_out_project.txt`)**:

   - After defining your app’s structure, use this template to create a skeleton of your project. This phase focuses on setting up the basic architecture and stubbing out essential components, leaving placeholders for further development.

3. **Fully Code Out Implementation (`3_fully_code_out_implementation.txt`)**:
   - This template will guide you in transforming the stubbed-out project from Phase 2 into fully functional, production-ready code. You'll focus on implementing core features, building out your app, and making sure everything is well-structured and scalable.

## Steps performed
SZ
### Phase 1 creation Master plan
1. **submit to cause 1_generate_master_plan.txt  long prompt**
   - claude ask for my replys
2. enter the prompt below and attache 4 images from aunder resources/design/img  
```txt
I'm creating a next JS projectr and I need your help turning my drawings into real life next JS code. Just to give you a little bit more background about the project.  I am trying to automate my workflow with the help of AI so that I can upload video clips, and then configure some prompots  and then trigger a bunch of Lang chain runs to go off and summarize all of my YouTube videos and gnerate post for LinkedIn, Twitter, YouTube, and a munch more places. 

I'm uploading pictures of what of a few key wireframes of the app.
```

NB! Claude accepts up to 5 images 

3.  enter the prompt below  for corrections and additional info
```txt
Corrections & Additional Information:
- There will be a flask BE component. not a Flash.
- | only uploaded information for the upload stage. However, we will
eventually need to build out the config, run, and result tabs as well.
- The stage content here is a place holder for the different Upload, Config,
Run, Result stages

Answers to Your Questions:

1. | want to be able to upload a bunch of clips. Have an Al transcribe them.
Once we have all the transcriptions, summarize all of the transcriptions
into a 2,000 word summary. I'd like to use OpenAl for all of this. Do you
have any suggestions on how we can do this?

2. Upload stage - Upload all of the clips and store them in a blob store.
Config Stage - In this stage, | want to create and edit the prompts required
to convert the summary of the video clips into posts for X, LinkedIn,
YouTube, etc. Run Stage - This is where | should be able to trigger a run

3. No.

4. I want to use Clerk. only individuals will use this app. No need to setup organizations.

5. Notat this time.

6. Which recomendations do you have? I want to use something simple, cheap,and easy to understand.

7. I think we need to have some sort of job that is craeted when the user triggers a run. This run will have a status of Ready.  The Python Backend  needsto be polling for ready jobs and then start working on them. As the backend starts to work on the job, it needs to update the state of the job to Running.

Do you have any followup questions? Do I need to elaborate more on any of my feedback or answers?
```

4. provide next round of answers to questions , enter the prompt
```
Below are my answers

project summary points
1.  sounds good!
6. Let's use UploadThing instead
7. Simple database

follow up questions:
1. Postgresql
2. up to 10 concurrrent users, each uploading up to 100 videos
3. No preference for frontend. I'll let you recommend
4. Lets stay with rest
5. store status  OK|Failed for each processed video file
6. standard logging for now
7. lets stay now with unit tests
```

5. 
```
You now know enough, please generate  the masterplan.md file
```
Download the generated md file  and save it under `resources/plan/masterplan.md`

**The goal is to generate a high quality masterplan.md**

### Phase 2 Stub Out the files

1. Create  new claude project named Youtube Content Automation
upload  to Project knowlege our `app_masterplan.md`.
On the left chat  click on add content to upload our design wireframe images.

In the chat  copy a text from template `2_stub_out_project.txt`

2. answer
```
Proceed with creating the project structure. 
Write a bash script  to create project directory structure and stub files.
```
3. copy and review project-setup.sh  save it in resources/sh/project-setup.sh

4. enter prompt
```
based on reviewed project-setup.sh please create file stubs in typescript and  python
```
5. copy stub files in their respective location in a  project

6. add all stußbs to project  knowlege
ß
### Phase 3 
1. in the same chat  add the  3_fully_code_out_implementation.txt 
2.  add th first prompt
 ```
The first page I need help with is the root page app/page.tsx. Currently, this page is very bland. I would like you to make this page look modern and stylish. Add a hero section to greet the user, let them know about the app, and then have a CTA which directs them to their projects. For the color scheme, I want to use rose-500, dark gray, and white.
 ```
save the proposed content  to a file.

then reappload this file  to  Project contents. 


the cycle:  


End of course:   there is a demo of an actuall app


