namespace ExerciseOopHierarchy;

public abstract class MenuItem
{
    //артикул от менюто -> име, описание, цена

    //състояние / характеристики -> полета / property
    public string Name { get; set; }
    public string Description { get; set; }
    public decimal Price { get; set; }


    //конструктор -> създава обект от класа
    public MenuItem(string name, string description, decimal price)
    {
        //нов празен обект
        Name = name;
        Description = description;
        Price = price;
    }

    //поведение / дейности
    //ToString -> обекта под формата на текст -> "ExerciseOopHierarchy.MenuItem"
    public override string ToString()
    {
        return $"{this.Name} - {this.Description} - ${this.Price}";
    }

}
