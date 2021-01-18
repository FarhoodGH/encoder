<h1 style="color:darkcyan;">Encoder (C# Version)</h1>
Author : [@Ali Javadi](https://github.com/javadimoghadam/)

## Package's Content :
> ~/dll source/encoderDLL.dll -> MD5 : c35b93eb0cc4e467b9596a1f5f51b419


> ~/encoder.sln -> MD5 : a5dc7404abf4fca39cc59b5397047b39

## How to use
If you Have visual studio on your system :

```bash
cd "C# Version"
start encoder.sln
```

If you Just Run dev on your system :

```bash
cd "C# Version"\encoder\bin\Debug
start encoder.exe
```

<h2 style="color:darkcyan;font-weight:bold;">How to use .dll file (Docuemention)</h2>

> Add .dll file in your Project

Build a Code
```cs
using encoderDLL;

var tools = new encode();
```

Use for Encode
```cs
var text = "Test Text ! Lorem Ipsom";
Console.WriteLine(tools.Encode(text));
```

----------------------------------------

Use for Decode
```cs
var text = "R3JmZyBHcmtnICEgWWJlcnogVmNmYno=";
Console.WriteLine(tools.Dncode(text));
```