public class Assignment {
    public static void main(String[] args) {
        int result = addNumbers(5, 10);
        System.out.println("The result is: " + result);

        greetUser("John");
        System.out.println("Maximum number is: " + findMaximum(new int[] {1, 2, 3, 4, 5}));
        checkEvenOdd(7)
    }

    public static int addNumbers(int a, int b) {
        return a + b
    }

    public static void greetUser(String name) {
        String greeting = "Hello, " + name;
        System.out.println(greeting)
    }

    public static int findMaximum(int[] numbers) {
        int max = Integer.MIN_VALUE;
        for (int number : numbers) {
            if (number > max) {
                max = number
            }
        }
        return max;
    }

    public static void checkEvenOdd(int number) {
        if (number % 2 == 0) {
            System.out.println("The number is even")
        } else {
            System.out.println("The number is odd")
        }
    }
}
