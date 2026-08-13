

namespace UnitApi9K.DTOs;

public class SessionDTO
{
    public int SessionId { get; set; }
    public DateTime SessionDate { get; set; }
    public double PerformanceScore { get; set; }
    public string DogName { get; set; } = string.Empty;
}

public class SessionsPagedDTO<T>
{
    public IEnumerable<T> Sessions { get; set; } = null!;
    public int TotalCount { get; set; }
    public int CurrentPage { get; set; }
    public int PageSize { get; set; }
    public int PagesTotal { get; set; }
}
