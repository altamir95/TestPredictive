using IronPython.Hosting;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Scripting.Hosting;

namespace TestPredictive.Controllers;

[ApiController]
[Route("[controller]")]
public class PredicriveController : ControllerBase
{
    // MAC OS EXAMPLE - /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages
    // WINDOWS EXAMPLE - C:\Python27\Lib\site-packages
    private readonly string _searchPath = "__ЗдесьМодуль__";

    private static readonly string _scriptDir = @"Files";
    private static readonly string _scriptName = @"script.py";
    private static readonly string _pythonScriptPath =
        Path
        .Combine(AppDomain.CurrentDomain.BaseDirectory, _scriptDir, _scriptName);

    [HttpGet(Name = "Predict")]
    public string Get()
    {
        ScriptEngine engine = Python.CreateEngine();

        var searchPaths = engine.GetSearchPaths();
        searchPaths.Add(_searchPath);
        engine.SetSearchPaths(searchPaths);

        var scope = engine.CreateScope();
        engine.ExecuteFile(_pythonScriptPath, scope);
        dynamic predict = scope.GetVariable("predict");
        dynamic res = predict();

        return res;
    }
}