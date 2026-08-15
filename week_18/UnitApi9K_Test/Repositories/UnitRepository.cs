using UnitApi9K.Models;
using UnitApi9K.Enums;
using UnitApi9K.Data;
using UnitApi9K.DTOs;
using System.Globalization;
using Microsoft.EntityFrameworkCore;
using UnitApi9K.Exceptions;

namespace UnitApi9K.Repositories;

public class UnitRepository : IUnitRepository
{
    private readonly AppDbContext _context;

    public UnitRepository(AppDbContext context)
    {
        _context = context;
    }

    // Create new dog
    public async Task<GetDogDTO> CreateDogAsync(PostDogDTO dog)
    {
        if (await _context.Dogs.AnyAsync(d => d.MicrochipId == dog.MicrochipId))
        {
            throw new ExistedMicroshipId();
        }

        var created = new Dog
        {
            Name = dog.Name,
            Breed = dog.Breed,
            MicrochipId = dog.MicrochipId,
            DateOfBirth = dog.DateOfBirth,
            Specialty = dog.Specialty,
            Status = dog.Status
        };

        _context.Dogs.Add(created);
        await _context.SaveChangesAsync();

        return new GetDogDTO
        {
            Id = created.Id,
            Name = dog.Name,
            Breed = dog.Breed,
            MicrochipId = dog.MicrochipId,
            DateOfBirth = dog.DateOfBirth,
            Specialty = dog.Specialty,
            Status = dog.Status
        };
    }

    // Get existed dog by id
    public async Task<GetDogDTO?> GetDogByIdAsync(int id)
    {
        var dog = await _context.Dogs.FindAsync(id);

        if (dog == null)
        {
            return null;
        }

        return new GetDogDTO
        {
            Id = id,
            Name = dog.Name,
            Breed = dog.Breed,
            MicrochipId = dog.MicrochipId,
            DateOfBirth = dog.DateOfBirth,
            Specialty = dog.Specialty,
            Status = dog.Status
        };
    }

    // Create new training
    public async Task<GetTrainingSessionDTO> CreateTrainingAsync(
        PostTrainingSessionDTO training)
    {   
        var created = new TrainingSession
        {
            DogId = training.DogId,
            SessionDate = training.SessionDate,
            DurationMinutes = training.DurationMinutes,
            TrainingType = training.TrainingType,
            PerformanceScore = training.PerformanceScore,
            Passed = training.PerformanceScore >= 75 ? true : false,
            Evaluator = training.Evaluator
        };
        _context.TrainingSessions.Add(created);
        await _context.SaveChangesAsync();

        return new GetTrainingSessionDTO
        {
            Id = created.Id,
            DogId = created.DogId,
            SessionDate = created.SessionDate,
            DurationMinutes = created.DurationMinutes,
            TrainingType = created.TrainingType,
            PerformanceScore = created.PerformanceScore,
            Evaluator = created.Evaluator,
            Passed = created.Passed
        };
    }

    // Delete existed handler
    public async Task<bool> DeleteHandlerAsync(int id)
    {
        var handler = await _context.Handlers.FindAsync(id);
        if (handler == null)
        {
            return false;
        }

        _context.Handlers.Remove(handler);
        await _context.SaveChangesAsync();

        return true;
    }

    // Query 1 - Get filterd dogs
    public async Task<IEnumerable<FilterdDogDTO>> SearchAsync(
        SpecialtyTypes? specialty, StatusTypes? status)
    {
        var query = _context.Dogs.AsQueryable();

        if (specialty.HasValue)
        {
            query = query.Where(d => d.Specialty == specialty);
        }
        if (status.HasValue)
        {
            query = query.Where(d => d.Status == status);
        }

        return await query.Select(d => new FilterdDogDTO
        {
            Id = d.Id,
            Name = d.Name,
            Breed = d.Breed,
            Specialty = d.Specialty,
            Status = d.Status
        }).ToListAsync();
    }

    // Query 2 - Get dogs with handlers
    public async Task<IEnumerable<DogWithHanlerDTO>> GetDogsWithHandlersAsync()
    {
        return await _context.Dogs
            .Select(d => new DogWithHanlerDTO
            {
                DogId = d.Id,
                DogName = d.Name,
                Breed = d.Breed,
                Specialty = d.Specialty,
                Status = d.Status,
                HandlerName =  d.Handler.FullName,
                HandlerRank = d.Handler.Rank
            }).ToListAsync();
    }

    // Query 3 - Get summery performance
    public async Task<IEnumerable<SummeryPerformanceDTO>> 
        GetSummeryPerformanceAsync()
    {
        return await _context.Dogs
            .Select(d => new SummeryPerformanceDTO
            {
                DogId = d.Id,
                DogName = d.Name,
                Specialty = d.Specialty,
                TrainingsCount = d.Trainings.Count,
                AveragePerformance = d.Trainings.Count > 0 ?
                d.Trainings.Average(t => t.PerformanceScore): null
            }).ToListAsync();
    }

    // Get all training sessions with detailes
    public async Task<IEnumerable<TrainingDetailesDTO>>
        GetTrainigSessionsDetailesAsync()
    {
        return await _context.TrainingSessions
            .Select(t => new TrainingDetailesDTO
            {
                Id = t.Id,
                DogId = t.DogId,
                DogName = t.Dog.Name,
                Specialty = t.Dog.Specialty,
                SessionDate = t.SessionDate,
                DurationMinutes = t.DurationMinutes,
                TrainingType = t.TrainingType,
                PerformanceScore = t.PerformanceScore,
                Passed = t.Passed,
                Evaluator = t.Evaluator,
                HandlerName = t.Dog.Handler.FullName
            }).ToListAsync();
    }

    // Get Paged of training sessions
    public async Task<SessionsPagedDTO<SessionDTO>>
        GetPagedAsync(int page, int pageSize)
    {
        var totalCount = await _context.TrainingSessions.CountAsync();

        var items = await _context.TrainingSessions
            .OrderByDescending(t => t.SessionDate)
            .Skip(page != 0 ? (page - 1) * pageSize : 0)
            .Take(pageSize)
            .Select(t => new SessionDTO
            {
                SessionId = t.Id,
                SessionDate = t.SessionDate,
                PerformanceScore = t.PerformanceScore,
                DogName = t.Dog.Name
            }).ToListAsync();

        return new SessionsPagedDTO<SessionDTO>
        {
            Sessions = items,
            TotalCount = totalCount,
            CurrentPage = page,
            PageSize = pageSize,
            PagesTotal = pageSize != 0 ? 
            (int)Math.Ceiling((double)totalCount / pageSize) :
            0
        };
    }
}
