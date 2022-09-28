<h1>
    Git 고급
</h1>

<h3>
    Git Pull Request
</h3>


> 로컬 저장소에 브랜치를 생성해서 같은 원격 저장소에 푸시하는 경우, 충돌이 발생할 수 있으므로 `pull request`를 통해 원격 저장소에 `merge`를 요청
>

<h5>
    <span style="font-style: bold ;"> Fork </span>
</h5>
* 가져오고자 하는 저장소를 자신의 저장소로 `Fork`
  * `Fork`할때는 자신의 저장소로 가져옴
<h5>
    <span style="font-style: bold ;"> Clone  </span>
</h5>
* `Fork`로 생성한 저장소에서 `clone or download`로 URL을 복사

  * `clone`하면 폴더 생성됨(`git bash`이용)

  ```bash
  $ git clone {복사한 URL}
  
  /Users/DonghyeonKang - (master) > cd Desktop # Desktop으로 이동 후 폴더 생성
  $ git clone https://github.com/kangdh208/folderforpull.git
  ```

<h5>
    <span style="font-style: bold ;"> branch 만들기  </span>
</h5>	
* PC에 `clone`된 저장소(`origin`)에서 작업하는 branch를 만들어 진행
```bash
$ git branch {branch name}
$ git branch example

Desktop/forderforpull - (master) > git branch example
```
* branch 생성 후 이동
```bash
$ git checkout {branch name}
$ git checkout example

Desktop/forderforpull - (master) > git checkout example
Switched to branch 'example'
Desktop/forderforpull - (example) > # master -> example로 branch가 이동됨
```
<h5>
    <span style="font-style: bold ;"> 작업 후 PUSH  </span>
</h5>	
* 작업 후 `add`, `commit`, `push`
```bash
Desktop/forderforpull - (example) > git add .
Desktop/forderforpull - (example) > git commit -m "modify"
Desktop/forderforpull - (example) > git push origin example
```
> 작업 후 `Github Repository(origin)`에 `push`
> `push`할때 `develop`브랜치의 수정내용을 `origin`으로 푸시
<h5>
    <span style="font-style: bold ;"> Pull Request  </span>
</h5>	
* `push`후 자신의 깃허브 저장소의 `Compare & pull request`버튼(활성화 되어있음)을 통해 `Pull requests`보내기
<h5>
    <span style="font-style: bold ;"> Merge Pull Request  </span>
</h5>	
* 작업 관리자 계정은 요청온 작업의 내용확인 후에 `Merge` 혹은 `reject`
<h5>
    <span style="font-style: bold ;"> Merge 후 branch 삭제  </span>
</h5>	
* `merge`가 완료되면 로컬코드와 원본코드를 병합하고 동기화
* `upstream`확인
```bash
$ git remote -v 
```
* `upstream`추가
```bash
$ git remote add upstream
$ git fetch upstream
$ git merge upstream/master
$ git branch -d example
```
* `branch` 삭제

**Git : `Shared repository` vs `Folk and pull repository` **

> 권한의 차이. Shared Repository와는 다르게 Fork & Pull Request는 마음대로 수정, 삭제가 불가능. 그래서 원격 저장소를 Fork 한 후에 로컬 저장소로 가져와 clone하고 branch를 생성 한 뒤에 작업을 끝마치면 Pull Request를 하여 Fork한 원작자의 승인을 받으면 병합이 됨

<h3>
    Git.gitignore File
</h3>

> `.gitignore` 이란 프로젝트에 원치않는 파일들을 `git`에 제외시킬 수 있는 설정 파일

* *원치않는 파일들 예시* 

  * 보안상 위험성이 높은 파일

  * 프로젝트와 관계없는 파일

  * 용량이 너무 큰 파일

  * 백업 파일 등

1. **gitignore 파일 만들기**          >>주의!!         *항상 최상위 디렉토리에 존재해야 함

<img src='C:\Users\Donghyeon Kang\Desktop\TIL\1week\git_고급.assets\vi_create.png'>

2. **gitignore 파일에 한 줄씩 제외할 파일이나 폴더 적기**

![vi img](C:\Users\Donghyeon Kang\Desktop\TIL\1week\git_고급.assets\Vi_ignore.png)



<h3>
    Git.gitkeep
</h3>
> `.gitkeep` 이란  `git`사용자가 만든 빈 파일. `Git` 저장소가 빈 프로젝트 디렉토리를 유지.
>
> A라는 빈폴더를 생성하고 커밋하려고 해도 A폴더는 `Git` 저장소에 커밋되지 않지만 `gitkeep`파일을 A폴더에 넣으면 커밋 가능. 삭제할 때도 `gitkeep` 있으면 커밋할 때 없어지지 않고 유지됨



<h3>
    Authority
</h3>

<h5>
    Shared Repository vs Folk and Pull Repository
</h5>

> `Shared Repository Model` 는 권한을 갖은 상태에서 `pull`. 
>
> `Shared Repository Model`에서 작업에 대한 수정을 요할 때 `collaborator`에게는 단일공유저장소와 토픽브랜치가 생성됨. `pull requests`는 코드를 리뷰할때와 작업에 대한 수정내용을 통합브랜치에 `merge`하기 전에 수정한 방향에 대한 토론을 할때 유용함. 소규모 프로젝트와 프라이빗한 프로젝트에 유용

> `Folk & Pull Repository Model` 는 권한이 없는 상태에서 `pull`. 
>
> `Folk & Pull Repository Model`에서는 누구나 이미 존재하는 저장소에 대해 `fork`를 할 수 있고 수정 작업을 `push`할 수 있음. 소스코드가 있는 저장소에 대해 소유주에게 `fork`에 대한 허가가 필요하지 않으며 수정작업은 프로젝트를 유지하는 사람은 누구나 `push`할 수 있음. 이 모델은 새 `contributors`와의 많은 마찰을 줄이면서, 사전조정이 필요하지 않으므로 개개인이 독립적인 작업을 할 수 있게하므로 오픈소스프로젝트에 적합함

* 용어정리
  * `Contributor` : 관리자. `push`와 `pull`, `merge`에 대한 허용권한등을 갖고 있는 사람
  * `Collaborator` : `push`와 `pull` 권한을 모두 가지고 있는 사람, `contributor`와 달리 관리자가 직접 추가해줘야 얻을 수 있는 권한
  * 통합브랜치(`Integration branch`) : 언제라도 배포할 수 있는 버전을 만들 수 있어야 하는 브랜치, 중앙브랜치, 일반적으로 `master branch`를 통합브랜치로 사용
  * 토픽브랜치(`Topic branch`) : 기능 추가나 버그 수정과 같은 단위 작업을 위한 브랜치, 피처브랜치(`feature branch`)라고도 부름
  * 단일공유저장소 : `single shared repository` .
