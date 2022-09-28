<h1>
    Git 초급
</h1>
<h3>
    Git Push
</h3>


> `git push` 는 `local repository`(로컬저장소)에 있는 변경이력을 원격 저장소에 전송하는 명령어

```bash
$ git push <저장소명> <브랜치명>
```
* -u 옵션
  * 최초에 한 번만 저장소명과 브랜치 명을 입력하고 그 이후 모든 인자 생략 가능
<h3>    Git Branch & Merge</h3>
> `Branch` 는

```bash 
#branch name 미 입력시 브랜치 목록 조회
(master) $ git branch {branch name}
(master) $ git branch --all # 서버에 있는 모든 브랜치 목록 확인
(master) $ git branch example
#branch 이동
(master) $ git checkout {branch name}
(master) $ git switch {branch name}
(master) $ git checkout example
#branch 생성하면서 이동
(master) $ git checkout -b {branch name}
(master) $ git switch -b {branch name}
(master) $ git checkout -b example
#branch 삭제
(master) $ git branch -d {branch name}
(master) $ git push origin --delete # 서버에 있는 브랜치 삭제
(master) $ git branch -d example
#branch 목록
(master) $ git branch
```

> `Merge` 는  `branch`로 분기된 각 `commit`을 하나로 다시 합치고싶을 때 사용하는 명령어
```bash
#master에 merge가 완료되었으면 branch를 삭제해도 됨
(master) $ git merge {branch name}
(master) $ git merge example
#merge 취소
(master) $ git merge --abort
#병합하면서 해당 branch기록을 남기고 싶을 경우
(master) $ git merge --no-ff
#branch 확인
$ git branch --merged # 현재 브랜치에 머지가 된 브랜치 확인
$ git branch --no-merged # 마스터 브런치에서 파생된 브랜치 학인
```

