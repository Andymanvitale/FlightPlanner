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

