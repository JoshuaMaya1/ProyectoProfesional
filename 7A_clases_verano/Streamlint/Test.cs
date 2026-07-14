using System;

public interface ISaludable
{
    void Saludar();
}

public abstract class Ser
{
    public abstract void Existir();
}

public class Persona : Ser, ISaludable
{
    private string nombre;
    public int edad;

    public Persona(string nombreParam, int edadParam)
    {
        nombre = nombreParam;
        edad = edadParam;
    }

    public void Saludar()
    {
        Console.WriteLine("Hola");
    }

    public override void Existir()
    {
        if (edad >= 18)
        {
            Console.WriteLine("Mayor de edad");
        }
        else
        {
            Console.WriteLine("Menor de edad");
        }
    }

    public void Riesgo()
    {
        try
        {
            int resultado = 10;
        }
        catch (Exception error)
        {
            Console.WriteLine("Error detectado");
        }
    }
}
