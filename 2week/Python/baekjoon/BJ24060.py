# 오늘도 서준이는 병합 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 병합 정렬로 배열 A를 오름차순 정렬할 경우 배열 A에 K 번째 저장되는 수를 구해서 우리 서준이를 도와주자.

# 크기가 N인 배열에 대한 병합 정렬 의사 코드는 다음과 같다.

# merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
#     if (p < r) then {
#         q <- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
#         merge_sort(A, p, q);      # 전반부 정렬
#         merge_sort(A, q + 1, r);  # 후반부 정렬
#         merge(A, p, q, r);        # 병합
#     }
# }

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.

# merge(A[], p, q, r) {
#     i <- p; j <- q + 1; t <- 1;
#     while (i ≤ q and j ≤ r) {
#         if (A[i] ≤ A[j])
#         then tmp[t++] <- A[i++]; # tmp[t] <- A[i]; t++; i++;
#         else tmp[t++] <- A[j++]; # tmp[t] <- A[j]; t++; j++;
#     }
#     while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
#         tmp[t++] <- A[i++];
#     while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
#         tmp[t++] <- A[j++];
#     i <- p; t <- 1;
#     while (i ≤ r)  # 결과를 A[p..r]에 저장
#         A[i++] <- tmp[t++]; 
# }

N,K = map(int, input().split())
A = list(map(int, input().split()))

