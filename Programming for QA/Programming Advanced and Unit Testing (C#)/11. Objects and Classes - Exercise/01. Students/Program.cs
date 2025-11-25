class Student
{
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public double Grade { get; set; }

    public Student(string firstName, string lastName, double grade)
    {
        FirstName = firstName;
        LastName = lastName;
        Grade = grade;
    }

    public override string ToString()
    {
        return $"{FirstName} {LastName}: {Grade:F2}";
    }
}

class Program
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        List<Student> students = new List<Student>();

        for (int i = 0; i < n; i++)
        {
            string[] studentInfo = Console.ReadLine().Split(' ');
            string firstName = studentInfo[0];
            string lastName = studentInfo[1];
            double grade = double.Parse(studentInfo[2]);

            students.Add(new Student(firstName, lastName, grade));
        }

        students = students.OrderByDescending(s => s.Grade).ToList();

        foreach (var student in students)
        {
            Console.WriteLine(student);
        }
    }
}