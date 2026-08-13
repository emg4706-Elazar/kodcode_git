using Microsoft.AspNetCore.Mvc;
using UnitApi9K.DTOs;
using UnitApi9K.Enums;
using UnitApi9K.Models;
using UnitApi9K.Repositories;

namespace UnitApi9K.Controllers;


[ApiController]
[Route("api/handlers")]
public class HandlersController : ControllerBase
{
    private readonly IUnitRepository _repo;
    public HandlersController(IUnitRepository repo)
    {
        _repo = repo;
    }

    // Delete existed handler
    [HttpDelete("{id}")]
    public async Task<IActionResult> DeleteHandler(int id)
    {
        var success = await _repo.DeleteHandlerAsync(id);
        if (!success)
        {
            return NotFound();
        }

        return NoContent();
    }
}
