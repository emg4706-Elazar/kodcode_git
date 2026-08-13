using UnitApi9K.DTOs;
using UnitApi9K.Models;
using UnitApi9K.Enums;

namespace UnitApi9K.Repositories;

public interface IUnitRepository
{
    Task<GetDogDTO> CreateDogAsync(PostDogDTO dog);
    Task<GetDogDTO?> GetDogByIdAsync(int id);
    Task<GetTrainingSessionDTO> CreateTrainingAsync(PostTrainingSessionDTO training);
    Task<bool> DeleteHandlerAsync(int id);
    Task<IEnumerable<FilterdDogDTO>> SearchAsync(
        SpecialtyTypes? specialty, StatusTypes? status);
    Task<IEnumerable<DogWithHanlerDTO>> GetDogsWithHandlersAsync();
    Task<IEnumerable<SummeryPerformanceDTO>> GetSummeryPerformanceAsync();
    Task<IEnumerable<TrainingDetailesDTO>> GetTrainigSessionsDetailesAsync();
    Task<SessionsPagedDTO<SessionDTO>> GetPagedAsync(int page, int pageSize);
}
