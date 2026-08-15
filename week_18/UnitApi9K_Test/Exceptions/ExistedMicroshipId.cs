

namespace UnitApi9K.Exceptions;

public class ExistedMicroshipId : Exception
{
    public ExistedMicroshipId()
        : base("This MicroshipId is already existed.")
    {
    }
}
