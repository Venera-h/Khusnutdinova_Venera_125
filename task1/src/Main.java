import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Task 1");
        System.out.print("Введите число ");
        double n = scanner.nextDouble();
        long roundN = Math.round(n);
        System.out.println(roundN);
        obmen();
        temperatura();//3
        vclad();//4
        evenNumbers();//5
        evenOrNo();//6
        tickets();
        equation();//8
        factorial();//9
        count();//10
        countEven();//11
        max();//12
        numberOfYear();//13
        function();//14
        money();//15
        iceCream();//16

    }

    public static void obmen() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Task 2");
        System.out.println("Введите cумму в $");
        double dollar = scanner.nextDouble();
        double pound = dollar/1.487; //фунты
        double franc = dollar/0.172; //франки
        double mark = dollar/0.584; //немецкие марки
        double yen = dollar/0.00955; //японская йена
        System.out.println("Вы получите " + pound +
    " фунта, " + franc + " франков, " + mark + " немецкой марки, " + yen + " йен");

    }


    public static void temperatura() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Task 3");
        System.out.println("Введите температуру в градусах Цельсия:");
        double t = scanner.nextDouble();//градусы по цельсию
        double T = (t * 9) / 5 + 32;
        System.out.println("Эквивалент по Фаренгейту - " + T);
    }

    public static void vclad() {
        System.out.println("Task 4");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите начальную сумму вклада: ");
        double money = scanner.nextDouble();
        System.out.print("Процент вклада: ");
        double percent = (scanner.nextDouble() / 100);
        System.out.print("Количество лет: ");
        int year = scanner.nextInt();
        for (int count = 1; count <= year; count++) {
            double numberOfMoney = money * percent;
            money += numberOfMoney;
        }
        System.out.println("Через " + year + " года можно получить " + money + " рублей");
    }

    public static void evenNumbers() {
        System.out.println("Task 5");
        for (int i = 26; i <= 62; i += 2) {
            System.out.println(i);
        }
    }

    public static void evenOrNo() {
        System.out.println("Task 6");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите число");
        int n = scanner.nextInt();
        if (n % 2 != 0) {
            System.out.println("Число нечетное");
        } else {
            System.out.println("Число четное");
        }
    }
    public static void tickets(){
        System.out.println("Task 7");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите число билетов");
        int n = scanner.nextInt();
        int money = 0;
        int cost_1 = 0; // количество билетов по 1 поездке
        int cost_5 = 0; //количество билетов по 5 поездок
        int cost_10 = 0; // количество билетов по 10 поездок
        int cost_20 = 0; // количество билетов по 20 поездок
        int cost_60 = 0; // количество билетов по 60 поездок

        while (n > 0) {
            if (n >= 60) {
                cost_60 += 1;
                n -= 60;
                money += 440;
            } else if (n >= 20) {
                cost_20 += 1;
                n -= 20;
            }else if (n >= 10) {
                cost_10 += 1;
                n -= 10;
            } else if (n >= 5) {
                cost_5 += 1;
                n -= 5;
            }  else if (n < 5) {
                cost_1 += 1;
                n -= 1;
            }
        }

        System.out.print(cost_1);
        System.out.print(cost_5);
        System.out.print(cost_10);
        System.out.print(cost_20);
        System.out.print(cost_60);
    }


    public static void equation() { //ax+b=0
        System.out.println("Task 8");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите число a");
        int a = scanner.nextInt();
        System.out.println("Введите число b");
        int b = scanner.nextInt();
        int x = 0;
        if (a != 0) {
            x = -b / a;
            System.out.println(x);
        } else if (a == 0) {
            System.out.println("No");
        } else if (a == 0 && b == 0) {
            System.out.println("INF");

        }
    }

    public static void factorial() {
        System.out.println("Task 9");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите число n");
        int n = scanner.nextInt();
        int f = 1;
        while (n > 0) {
            f *= n;
            n -= 1;
        }
        System.out.println(f);
    }

    public static void count() {
        System.out.println("Task 10");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите число n");
        int n = scanner.nextInt();
        int sum = 0;
        while (n != 0) {
            sum = sum + n % 10;
            n /= 10;
        }
        System.out.println(sum);
    }

    public static void countEven() {
        System.out.println("Task 11");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите число a");
        int a = scanner.nextInt();
        System.out.println("Введите число b");
        int b = scanner.nextInt();
        System.out.println("Четные числа:");
        for (int i = a; i <= b; i++) {
            if (i % 2 == 0) {
                System.out.println(i);
            }
        }
    }

    public static void max() {
        System.out.println("Task 12");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите число a");
        int a = scanner.nextInt();
        System.out.println("Введите число b");
        int b = scanner.nextInt();
        if (a > b) {
            System.out.println(" Наибольшее число - " + a);
        } else {
            System.out.println(" Наибольшее число - " + b);
        }
    }

    public static void numberOfYear() {
        System.out.println("Task 13");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите номер года");
        int n = scanner.nextInt();
        System.out.println("Год високосный?");
        if ((n % 4 == 0 && n % 100 != 0) || (n % 400 == 0)) {
            System.out.println("Yes ");
        } else {
            System.out.println("No ");
        }
    }

    public static void function() {
        System.out.println("Task 14");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите x");
        int x = scanner.nextInt();
        int sign;

        if (x > 0) {
            sign = 1;
        } else if (x < 0) {
            sign = -1;
        } else {
            sign = 0;
        }
        System.out.println("sign(x) = " + sign);
    }

    public static void money() {
        System.out.println("Task 15");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите стоимость товара в руб");
        int a = scanner.nextInt();
        System.out.println("в коп");
        int b = scanner.nextInt();
        System.out.println("Введите сколько заплатил покупатель в руб");
        int c = scanner.nextInt();
        System.out.println("в коп");
        int d = scanner.nextInt();
        int kopeika_m = a * 100 + b; // цена продуктов в копейках
        int kopeika_p = c * 100 + d; // сколько днег дал покупаель в копейках
        int pokypka = kopeika_p - kopeika_m;
        System.out.println("Сдача " + pokypka / 100 + " руб. " + pokypka % 100 + "коп.");
    }

    public static void iceCream() {
        System.out.println("Task 16");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите количество шариков");
        int k = scanner.nextInt();
        if (k % 3 == 0 || k % 5 == 0 || k % 8 == 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

    }
}