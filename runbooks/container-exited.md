# Docker container exited or will not start
1. Run docker ps -a to see the status and exit code.
2. Run docker logs CONTAINER to read the error.
3. Run docker inspect CONTAINER and check State, ExitCode and OOMKilled.
4. Exit code meaning: 0 finished normally, 1 application error, 137 killed (often out of memory, 128 plus signal 9), 143 stopped by SIGTERM (128 plus 15), 139 segmentation fault.
5. Other causes: port already in use, wrong CMD or ENTRYPOINT, missing environment variables, volume permission problems, no disk space.
6. Run the image interactively with docker run -it IMAGE sh to see the error, then fix and restart.
