namespace Solution {
  class Program {
    static void Main(string[] args) {

      var a = int.Parse(Console.ReadLine()!);
      var b = int.Parse(Console.ReadLine()!);

      if (a < b) Console.WriteLine("-1");
      else if (a > b) Console.WriteLine("1");
      else Console.WriteLine("0");
    }
  }
}