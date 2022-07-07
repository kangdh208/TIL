<h1>
    Git 중급
</h1>



<h3>
    Git Branch & Merge
</h3>

> `Branch` 는 개발자들이 동시에 다양한 작업을 할 수 있게 해주는 기능. `branch`를 이용해 각자 독립적인 작업영역(`repository`)에서 작업 가능하며 작업 후 `merge`를 통해 하나의 버전으로 통합 가능.
>
> 소프트웨어 개발 시 개발자들은 동일한 소스코드를 공유해서 다루게 되기 때문에 만일 여러 사람이 동일한 소스코드를 기반으로 다른 작업 수행시에는 각각 서로 다른 버전의 코드로 나올 수 밖에 없음.


> Git 브랜치를 위해 root-commit을 발생시키고 진행해야함

```bash
$ git init
(master) $ touch README.md
(master) $ git add .
(master) $ git commit -m 'Init'
```


<h5>
    <span style="font-style: italic ;"> branch 명령어 </span>
</h5>

1. 브랜치 생성

   ```bash
   (master) $ git branch [branch.name]
   ```

2. 브랜치 이동

   ```bash
   (master) $ git checkout [branch.name]
   ```

3. 브랜치 생성 및 이동

   ```bash
   (master) $ git checkout -b [branch.name]
   ```

4. 브랜치 삭제

   ```bash
   (master) $ git branch -d [branch.name]
   ```

5. 브랜치 목록

   ```bash
   (master) $ git branch
   ```

6. 브랜치 병합

   ```bash
   (master) $ git merge [branch.name]
   ```

   * 병합하려는 주 브랜치에서 병합되는 브랜치인 `[branch.name]`을 병합

> `Merge` 는 `branch`로 분기된 각 `commit`을 하나로 다시 합치고싶을 때 사용하는 명령어

<h5>
    <span style="font-style: italic ;"> merge 명령어 </span>
</h5>

1. branch 병합
   ```bash
   master에 merge가 완료되었으면 branch를 삭제해도 된다.
   (master) $ git merge {branch name}
   (master) $ git merge example 
   ```

2. merge 취소
   ```bash
   (master) $ git merge --abort 
   ```

3. 병합하면서 해당 branch는 기록을 남기고 싶을때

   ```bash
   (master) $ git merge --no-ff
   ```

4. branch 확인

   ```bash
   $ git branch --merged # 현재 브랜치에 머지가 된 브랜치 확인
   $ git branch --no-merged # 마스터 브런치에서 파생된 브랜치 학인
   ```


<h5>
    <span style="font-style: italic ;"> head </span>
</h5>

> 이동한 `commit`의 정보를 표시

```bash
e2cdfa3 (HEAD -> master) add README # 예시
```

***
***
<h3>
    Git Branch 병합 시나리오
</h3>

<h5>
    Sit1. Fast-Forward
</h5>

> `fast-forward`는 주브랜치인 `master`브랜치에 변화가 없는 상태로 다른 변화가 생긴 `branch`로 `merge` 진행하게 되는 상황
>
> 새로운 `commit`이 생성되지 않은 상태로 `HEAD`의 위치만 변한 상태로 `merge` 대상의 마지막 `commit`에 주브랜치가 오게 됨

1. `feature/home branch`생성 및 이동

   ```bash
   (master) $ git branch feature/home #generate
   (master) $ git checkout feature/home #move
   ```

2. 작업완료 후 `commit`

   ```bash
   (feature/home) $ touch home.txt
   (feature/home) $ git add .
   (feature/home) $ git commit -m 'home.txt'
   (feature/home) $ git log --oneline
   ds32d34 (HEAD -> feature/home) Complete Home!!!!
   34e2dg2 (master) Init
   ```
   
3. `master`이동

   ```bash
   (feature/home) $ git checkout master
   ```

4. `master`에 병합

   ```bash
   (master) $git merge feature/home
   Updating 34e2dg2..ds32d34
   Fast-forward
   home.txt | 0
   1 file changed, 0 insertions(+), 0 deletions(-)
   create mode 100644 home.txt
   ```

5. `fast-forward` 

   ```bash
   (master) $ git log --oneline
   ds32d34 (HEAD -> master, feature/home) Complete Home!!!!
   34e2dg2 Init
   ```

6. `branch`삭제

   ```bash
   (master) $ git branch -d feature/home
   Deleted branch feature/home (was ds32d34).
   ```
***
<h5>
    Sit2. merge commit
</h5>


> `merge commit`는 서로 다른 `commit`을 `merge`하는 과정에 다른 파일이 수정되어 있는 상황으로 `git`이 `auto merging`을 진행하고 `commit`발생

1. `feature/about branch`생성 및 이동

   ```bash
   (master) $ git check out -b feature/about # 한번에 branch 생성 및 이동
   (feature/about) $
   ```

2. 작업완료 후 `commit`

   ```bash
   (feature/home) $ touch about.txt
   (feature/home) $ git add .
   (feature/home) $ git commit -m 'about.txt'
   (feature/home) $ git log --oneline
   90ab23d (HEAD -> feature/about) Complete about!!!!
   d23d25c Init
   ```
   
3. `master`이동

   ```bash
   (feature/home) $ git checkout master
   (master) $
   ```

4. `master`에 추가 `commit` 발생

   ```bash
   (master) $ touch maker.txt #다른 파일 수정/생성
   (master) $ git add .
   (master) $ git commit -m 'maker.txt'
   (master) $ git log --oneline
   38cda21 (HEAD -> master) Complete maker!!!!
   d2e1ced Init
   ```

5. `master` 에 병합 

   ```bash
   (master) $ git merge feature/about
   ```
   
6. 자동으로 `merge commit` 발생

7. `commit` & `graph` 확인

   ```bash
   $ git log --oneline --graph
   *   582902d (HEAD -> master) Merge branch 'feature/about'
   |\
   | * 582902d (feature/about) 자기소개 페이지 완료!
   * | 38cda21 마스터 작업....
   |/
   * 38cda21 Complete Merge!!!!
   * d2e1ced Init
   ```

6. `branch` 삭제

   ```bash
   (master) $ git branch -d feature/about
   Deleted branch feature/about (was 90ab23d).
   ```
***
<h5>
    Sit3. merge commit conflict
</h5>

> `merge commit`과정에서 같은 파일이 수정되어 있는 상황으로 `git`이 `auto merging`을 진행하지 못하고 `conflict` 메시지가 뜸
> 해당 파일의 위치에 표준형식에 따라 표시해주며 원하는 형태의 코드로 직접 수정을 하고 직접 `commit`을 발생시켜야함

1. `feature/about branch`생성 및 이동

   ```bash
   (master) $ git check out -b feature/test # 한번에 branch 생성 및 이동
   (feature/test) $
   ```

2. 작업완료 후 `commit`

   ```bash
   # README.md 파일 열어서 수정
   (feature/test) $ touch test.txt
   (feature/test) $ git add .
   (feature/test) $ git commit -m 'Add test.txt'
   (feature/test) $ git log --oneline
   95fad1c (HEAD -> feature/test) README 수정하고 test 작성하고
   582902d (master) Merge branch 'feature/about'
   98c5528 마스터 작업....
   5e1f6de 자기소개 페이지 완료!
   b534a34 Complete Home!!!!
   e89616a Init
   ```
   
3. `master`이동

   ```bash
   (feature/test) $ git checkout master
   (master) $
   ```

4. `master`에 추가 `commit` 발생
	
	*동일 파일을 수정/생성 해야함*
   
   ```bash
   # README.md 파일 열어서 수정
   (master) $ git add README.md
   (master) $ git commit -m 'Update README.md'
   ```

5. `master` 에 병합 

   ```bash
   (master) $ git merge feature/test 
   Auto-merging README.md
   CONFLICT (content): Merge conflict in README.md
   Automatic merge failed; fix conflicts and then commit the result.
   ```
   
6. 자동으로 `merge commit` 발생

   *git status 명령어로 충돌 파일을 확인할 수 있음*

   ```bash
   (master|MERGING) $ git status
   On branch master
   You have unmerged paths.
     (fix conflicts and run "git commit")        
     (use "git merge --abort" to abort the merge)
   
   Changes to be committed:
           new file:   test-1.txt
           new file:   test-2.txt
           new file:   test.txt
   
   Unmerged paths:
     (use "git add <file>..." to mark resolution)
           both modified:   README.md
   ```

7. 충돌 확인 및 해결

   ```
   <<<<<<< HEAD
   # 마스터에서 작업함...
   =======
   # 테스트에서 작성
   >>>>>>> feature/test
   ```

8. `merge commit` 진행

   ```bash
   (master|MERGING) $ git add .
   (master|MERGING) $ git commit
   ```
      * vim 편집기 화면이 나타납니다.

     * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
     * `w` : write
     * `q` : quit

9. 커밋 및 확인하기

   ```bash
   (master) $ git log --oneline --graph
   *   bc1c0cd (HEAD -> master) Merge branch 'feature/test'
   |\  
   | * 95fad1c (feature/test) README 수정하고 test 작성하고
   * | 2ecad28 리드미 수정
   |/  
   *   582902d Merge branch 'feature/about'
   |\  
   | * 5e1f6de 자기소개 페이지 완료!
   * | 98c5528 마스터 작업....
   |/  
   * b534a34 Complete Home!!!!
   * e89616a Init
   ```


10. branch 삭제

    ```bash
    (master) $ git branch -d feature/test
    ```