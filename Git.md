<h1> Git 실습 </h1>


<h3>
    사전 설정 (최초 한번) & TIP
</h3>

```bash
$ git config --global user.name 'GitHub ID'
$ git config --global user.email 'GitHub Email'
```
> 사전 설정 
user.name 은 github ID
user.email 은 github E-mail 권장

> 설정 확인 코드
```bash
$ git config --global --list
user.email=useremail@gmail.com
user.name=username
```
TIP
```html
git <명령어> --help 입력하면 git reference page 확인가능
예) git add --help 입력하면 git reference 에서 add 명령어 도움말 팝업
```

<h3>
    git init
</h3>
> `git init`은 새로운 Git 저장소(repository)를 생성할 때 사용하는 Git 명령어
>
> .git 라는 숨긴파일 생성 ->git 초기화 할때는 이 파일 삭제
<br>
* VS Code 에서 터미널을 Bash 로 설정
* 명령어 git init 입력

```bash
$ git init
Initialized empty Git repository in C:/Users/username/Desktop/TIL/.git/
```
<h3> git add & git status</h3>
> `git add` 는 다음 변경(commit)을 기록할 때까지 변경분을 모아놓기 위해서 사용
> `git status` 는 작업 디렉토리(working directory)와 스테이징 영역(staging area)의 상태를 확인하기 위해서 사용
<br>

```bash
$ git add .
```

```bash
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   Git.assets/GitFileLife.jpg
        new file:   Git.md
# Changes to be committed: 스테이징 영역에 넘어가 있는 변경 내용
# Changes not staged for commit: 아직 워킹 디렉토리에 있는 변경 내용
# Untracked files: 아직 워킹 디렉토리에 있는 파일 중 아직 한 번도 해당 Git 저장소가 관리한 적 없는 것
```

<h5>
    작업공간 구분
</h5>

<img style="max-height:65%; max-width:65%;" src="./Git.assets/GitFileLife.png">

**작업공간(working directory)**

> 작업공간은 실제 작업하고 있는 폴더를 의미 

**staging area**

> `commit` 되기 전의 작업물이 머무는 공간을 의미
>
> `working directory` 에 새롭게 추가된 파일이나 `commit` 이 된후 다시 변경된 파일이 `git add` 명령어를 통해 올라옴

**Repository**

> `commit` 이 된 작업물이 저장되는 공간


<h3>git commit & git log</h3>

> `git commit` 은 `staging area` 에 올라온 작업물을 Repository 에 최종기록하는 작업

> `git log`는 `repository`에 기록된 저장소 확인하는 명령어
<br>
```bash
$ git commit -m 'version name'
[master (root-commit) 3f46489] version name        
 2 files changed, 129 insertions(+)
 create mode 100644 Git.assets/GitFileLife.jpg
 create mode 100644 Git.md
 
$ git log
commit 3f464893765cgd4t5bdde227fd2a3i20u9cc13cf (HEAD -> master)
Author: username <useremail@gmail.com>
Date:   Tue Jul 5 16:18:46 2022 +0900

    version name
    
$ git log -1
commit 3f464893765cgd4t5bdde227fd2a3i20u9cc13cf (HEAD -> master)
Author: username <useremail@gmail.com>
Date:   Tue Jul 5 16:18:46 2022 +0900

    version name

```

TIP
```bash
$ git log -1 --oneline
3f46489 (HEAD -> master) version name
# log 를 최근 1개만 한줄로 출력
$ git log --oneline
3f46489 (HEAD -> master) Version name
# log 를 한줄로 출ㄹ겨
```
