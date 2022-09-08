<h1>
    BootStrap
</h1>


<h2>
    Web Programming
</h2>

* 웹프로그래밍
  * 프로그래밍 : 사람이 원하는대로 컴퓨터가 작동할 수 있도록 컴퓨터 언어로 명령어를 나열하는 행위
  * 웹 프로그래밍 : ‘웹 브라우저’와 관련된 프로그램을 작성하는 것
    * 백엔드 (back-end) 프로그래밍 : 서버에서 데이터 관리를 프로그래밍 
    * 프론트엔드(front-end) 프로그래밍 : 서버에서 받아온 정보를 웹 브라우저에 어떻게 표시할 것인지 프로그래밍

***

<h2>
    BootStrap
</h2>

- 다양한 종류의 input을 위한 picker를 제공
  - color : color picker
  - date : date picker
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정 (django 다룰때 다시함)
  - hidden : 사용자에게 보이지 않는 input

# Bootstrap

- CDN (Content Delivery Network)

  - 컨텐츠(CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템. 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점) 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐.

- spacing (Margin and padding)

  - **{property}{sides}-{size}**

  - mt - 3

    ```html
    <div class="mt-3 ms-5">bootstrap-sapcing</div>
    ```

  - {property}
    - m - for classes that set *margin*
    - p - for classes that set *padding*
  - {sides}
    - t - for classes that set margin-top or padding-top
    - b - for classes that set margin-bottom or padding-bottom
    - x - for classes that set both *-left and *-right
    - y - for classes that set both *-top and *-bottom
    - s - (start) for classes that set margin-left or padding-left in LTR(left to right), margin-right or padding-right in TRL
    - e - (end) for classes that set margin-right or padding-right in LTR, margin-left or padding-left in RTL
    - blank - for classes that set a margin or padding on all 4 sides of the element.
  - {size}
    - 0 - eliminate margin or padding : 0
    - 1 - set the margin or padding to $spacer *.25 (4px)
    - 2 - *0.5
    - 3 - equl to **1rem** (16px)
    - 4 - *1.5
    - 5 - *3
    - auto : auto (**블럭 요소 수평 중앙 정렬 가로 가운데 정렬** )

  ![Bootstrap](./bootstrap.png)



