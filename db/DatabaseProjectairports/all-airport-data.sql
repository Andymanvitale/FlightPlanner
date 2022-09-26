--Create a table
CREATE TABLE [dbo].[all-airport-data] (
    [Facility_Type]        NVARCHAR (50) NULL,
    [LocId]                NVARCHAR (50) NULL,
    [State_Id]             NVARCHAR (50) NULL,
    [County]               NVARCHAR (50) NULL,
    [City]                 NVARCHAR (50) NULL,
    [Name]                 NVARCHAR (50) NULL,
    [Use]                  NVARCHAR (50) NULL,
    [ARPLatitude]          NVARCHAR (50) NULL,
    [ARP_Latitude_Sec]     NVARCHAR (50) NULL,
    [ARPLongitude]         NVARCHAR (50) NULL,
    [ARP_Longitude_Sec]    NVARCHAR (50) NULL,
    [Elevation]            FLOAT (53)    NULL,
    [Magnetic_Variation]   NVARCHAR (50) NULL,
    [Sectional]            NVARCHAR (50) NULL,
    [Tie_In_FSS_Id]        NVARCHAR (50) NULL,
    [Tie_In_FSS_Name]      NVARCHAR (50) NULL,
    [FSS_Toll_Free_Number] NVARCHAR (50) NULL,
    [Fuel_Types]           NVARCHAR (50) NULL,
    [ATCT]                 NVARCHAR (50) NULL,
    [UNICOM]               FLOAT (53)    NULL,
    [CTAF]                 FLOAT (53)    NULL,
    [ICAOId]               NVARCHAR (50) NULL
);


GO

--Using the local database I set up, add all of the data to the db on this project
INSERT INTO [all-airport-data]
SELECT * FROM [airports].[dbo].[all-airport-data]


SELECT TOP (1000) [Facility_Type]
      ,[LocId]
      ,[State_Id]
      ,[County]
      ,[City]
      ,[Name]
      ,[Use]
      ,[ARPLatitude]
      ,[ARP_Latitude_Sec]
      ,[ARPLongitude]
      ,[ARP_Longitude_Sec]
      ,[Elevation]
      ,[Magnetic_Variation]
      ,[Sectional]
      ,[Tie_In_FSS_Id]
      ,[Tie_In_FSS_Name]
      ,[FSS_Toll_Free_Number]
      ,[Fuel_Types]
      ,[ATCT]
      ,[UNICOM]
      ,[CTAF]
      ,[ICAOId]
  FROM [all-airport-data]