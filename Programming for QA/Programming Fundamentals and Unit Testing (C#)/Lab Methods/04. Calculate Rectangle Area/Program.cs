int w = int.Parse(Console.ReadLine());
int l = int.Parse(Console.ReadLine());

Console.WriteLine(GetRectangleArea(w, l));


static int GetRectangleArea(int width, int lenght)
{
    int area = width * lenght;
    return area;
}
