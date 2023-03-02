FROM mcr.microsoft.com/dotnet/sdk:7.0 as build

WORKDIR /code/build

COPY *.csproj .
RUN dotnet restore

COPY . .
RUN dotnet publish -c Release -o /code/dist --no-restore

FROM mcr.microsoft.com/dotnet/runtime:7.0
WORKDIR /code/backend
COPY --from=build /code/dist /code/backend
ENTRYPOINT ["dotnet", "dotnetapp.dll"]