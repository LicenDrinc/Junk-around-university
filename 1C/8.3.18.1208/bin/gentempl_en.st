{1,
{3,
{"Standard",1,0,"",""},
{18,
{"Control",1,0,"",""},
{0,
{"If",0,0,"If","If <?""Condition""> Then

	<?>

EndIf;"}
},
{0,
{"IfElse",0,0,"If","If <?""Condition""> Then

	<?>

Else

	

EndIf;"}
},
{0,
{"While",0,0,"While","While <?""Condition""> Do

	<?>

EndDo;"}
},
{0,
{"For",0,0,"For","For <?""Counter""> To <?""Limit""> Do

	<?>

EndDo;"}
},
{0,
{"For Each",0,0,"For[ Each]","For Each <?""Variable""> In <?""Collection""> Do

	<?>

EndDo;"}
},
{0,
{"Procedure",0,0,"Proc[edure]","Procedure <?""Procedure Name"">()

	<?>

EndProcedure
"}
},
{0,
{"Procedure (with header)",0,0,"Proc[edure]","// <Procedure description>
//
// Parameters:
//  <Parameter1>  - <Type.Subtype> - <parameter description>
//                  <parameter description continued>
//  <Parameter2>  - <Type.Subtype> - <parameter description>
//                  <parameter description continued>
//
Procedure <?""Procedure Name"">()

	<?>

EndProcedure // <?""Procedure Name"">()
"}
},
{0,
{"Procedure in a form module",0,0,"Proc[edure]","// <Procedure description>
//
// Parameters:
//  <Parameter1>  - <Type.Subtype> - <parameter description>
//                  <parameter description continued>
//  <Parameter2>  - <Type.Subtype> - <parameter description>
//                  <parameter description continued>
//
&<?""Choose a compilation directive"", VariantChoice, ""AtClient"", ""AtClient"", ""AtServer"", ""AtServer"", ""AtServerNoContext"", ""AtServerNoContext"", ""AtClientAtServerNoContext"", ""AtClientAtServerNoContext"">
Procedure <?""Procedure Name"">()

	<?>

EndProcedure // <?""Procedure Name"">()"}
},
{0,
{"Procedure in a command module",0,0,"Proc[edure]","// <Procedure description>
//
// Parameters:
//  <Parameter1>  - <Type.Subtype> - <parameter description>
//                  <parameter description continued>
//  <Parameter2>  - <Type.Subtype> - <parameter description>
//                  <parameter description continued>
//
&<?""Choose a compilation directive"", VariantChoice, ""AtClient"", ""AtClient"", ""AtServer"", ""AtServer"", ""AtClientAtServer"", ""AtClientAtServer"">
Procedure <?""Procedure Name"">()

	<?>

EndProcedure // <?""Procedure Name"">()"}
},
{0,
{"Function",0,0,"Func[tion]","Function <?""Function name"">()

	<?>

EndFunction // <?""Function name"">()

"}
},
{0,
{"Function (with header)",0,0,"Func[tion]","// <Function description>
//
//
// Parameters:
//  <Parameter1>  - <Type.Subtype> - <parameter description>
//                 <parameter description continued>
//  <Parameter2>  - <Type.Subtype> - <parameter description>
//                 <parameter description continued>
//
// Returns:
//   <Type.Subtype>   - <returned value description>
//
Function <?""Function name"">()

	<?>

EndFunction // <?""Function name"">()
"}
},
{0,
{"Function in a form module",0,0,"Func[tion]","// <Function description>
//
//
// Parameters:
//  <Parameter1>  - <Type.Subtype> - <parameter description>
//                 <parameter description continued>
//  <Parameter2>  - <Type.Subtype> - <parameter description>
//                 <parameter description continued>
//
// Returns:
//   <Type.Subtype>   - <returned value description>
//
&<?""Choose a compilation directive"", VariantChoice, ""AtClient"", ""AtClient"", ""AtServer"", ""AtServer"", ""AtServerNoContext"", ""AtServerNoContext"", ""AtClientAtServerNoContext"", ""AtClientAtServerNoContext"">
Function <?""Function name"">()

	<?>

EndFunction // <?""Function name"">()"}
},
{0,
{"Function in a command module",0,0,"Func[tion]","// <Function description>
//
//
// Parameters:
//  <Parameter1>  - <Type.Subtype> - <parameter description>
//                 <parameter description continued>
//  <Parameter2>  - <Type.Subtype> - <parameter description>
//                 <parameter description continued>
//
// Returns:
//   <Type.Subtype>   - <returned value description>
//
&<?""Choose a compilation directive"", VariantChoice, ""AtClient"", ""AtClient"", ""AtServer"", ""AtServer"", ""AtClientAtServer"", ""AtClientAtServer"">
Function <?""Function name"">()

	<?>

EndFunction // <?""Function name"">()

"}
},
{0,
{"Return",0,0,"","Return;<?>"}
},
{0,
{"Try",0,0,"Try","Try

	<?>

Except

EndTry;"}
},
{0,
{"Compilation directive",0,0,"Direc[tive]","&<?""Choose a compilation directive"", VariantChoice, ""AtClient"", ""AtClient"", ""AtServer"", ""AtServer"", ""AtServerNoContext"", ""AtServerNoContext"", ""AtClientAtServer"", ""AtClientAtServer"", ""AtClientAtServerNoContext"", ""AtClientAtServerNoContext"">
"}
},
{0,
{"Instruction If",0,0,"Instr[ution]","#If <?""Choose a preprocessor instruction"", VariantChoice, ""Server"", ""Server"", ""Client"", ""Client"", ""ThinClient"", ""ThinClient"", ""WebClient"", ""WebClient"", ""ExternalConnection"", ""ExternalConnection"", ""ThickClientManagedApplication"", ""ThickClientManagedApplication"", ""ThickClientOrdinaryApplication"", ""ThickClientOrdinaryApplication""> Then
	<?>
#EndIf"}
},
{0,
{"Instruction Region",0,0,"#Reg[ion]","#Region <?>
	
#EndRegion"}
}
},
{18,
{"Applied",1,0,"",""},
{0,
{"Enumeration",0,1,"Enum[s]","PredefinedValue(""Enum.<?""Choose an enumeration value"", EnumValue>"")"}
},
{2,
{"Functional options",1,0,"",""},
{0,
{"Get a functional option",0,1,"Func[tional option]","GetFunctionalOption(""<?""Choose a functional option"", MetadataObject, ""FunctionalOption"">"")"}
},
{0,
{"Get an interface functional option",0,1,"Func[tional option]","GetInterfaceFunctionalOption(""<?""Choose a functional option"", MetadataObject, ""FunctionalOption"">"")"}
}
},
{4,
{"Common forms",1,0,"",""},
{0,
{"Open a common form",0,0,"Open[Form]","OpenForm(""CommonForm.<?""Choose a common form"", MetadataObject, ""CommonForm"">"");"}
},
{0,
{"Open a common form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""CommonForm.<?""Choose a common form"", MetadataObject, ""CommonForm"">"", FormParameters);"}
},
{0,
{"Get a common form",0,0,"Get[Form]","GetForm(""CommonForm.<?""Choose a common form"", MetadataObject, ""CommonForm"">"");"}
},
{0,
{"Get a common form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""CommonForm.<?""Choose a common form"", MetadataObject, ""CommonForm"">"");
"}
}
},
{5,
{"Exchange plans",1,0,"",""},
{0,
{"Open an exchange plan form",0,0,"Open[Form]","OpenForm(""ExchangePlan.<?""Choose an exchange plan"", ExchangePlan>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form."">"");"}
},
{0,
{"Open an exchange plan form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""ExchangePlan.<?""Choose an exchange plan"", ExchangePlan>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form."">"", FormParameters);"}
},
{0,
{"Get an exchange plan form",0,0,"Get[Form]","GetForm(""ExchangePlan.<?""Choose an exchange plan"", ExchangePlan>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form."">"");"}
},
{0,
{"Get an exchange plan form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""ExchangePlan.<?""Choose an exchange plan"", ExchangePlan>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form."">"", FormParameters);
"}
},
{0,
{"Items traversal",0,0,"","Selection = ExchangePlans.<?"""", ExchangePlan>.Choose();

While Selection.Next() Do

	<?>

EndDo;"}
}
},
{3,
{"Constants",1,0,"",""},
{0,
{"Get/Set",0,0,"Const[ants]","Constants.<?"""", Constant>.<?""Select variant"", VariantChoice, ""Get"", ""Get"", ""Set"", ""Set"">()"}
},
{0,
{"Set",0,0,"","Constants.<?"""", Constant>.Set(<?>);"}
},
{0,
{"Get",0,0,"","Constants.<?"""", Constant>.Get()"}
}
},
{6,
{"Catalogs",1,0,"",""},
{0,
{"Open a catalog form",0,0,"Open[Form]","OpenForm(""Catalog.<?""Choose a catalog"", Catalog>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Group form"", ""FolderForm"", ""Group choice form"", ""FolderChoiceForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Open a catalog form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""Catalog.<?""Choose Catalog"", Catalog>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Group form"", ""FolderForm"", ""Group choice form"", ""FolderChoiceForm"", ""Generic"", ""Form."">"", FormParameters);"}
},
{0,
{"Get a catalog form",0,0,"Get[Form]","GetForm(""Catalog.<?""Choose a catalog"", Catalog>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Group form"", ""FolderForm"", ""Group choice form"", ""FolderChoiceForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Get a catalog form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""Catalog.<?""Choose Catalog"", Catalog>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Group form"", ""FolderForm"", ""Group choice form"", ""FolderChoiceForm"", ""Generic"", ""Form."">"", FormParameters);
"}
},
{0,
{"Item traversal",0,0,"","Select = Catalogs.<?"""", Catalog>.Select();

While Select.Next() Do

	<?>

EndDo;"}
},
{0,
{"Items hierarchical traversal",0,0,"","Select = Catalogs.<?"""", Catalog>.SelectHierarchicaly();

While Select.Next() Do

	<?>

EndDo;"}
}
},
{6,
{"Documents",1,0,"",""},
{0,
{"Open a document form",0,0,"Open[Form]","OpenForm(""Document.<?""Choose a document"", Document>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Open a document form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""Document.<?""Choose a document"", Document>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form."">"", FormParameters);"}
},
{0,
{"Get a document form",0,0,"Get[Form]","GetForm(""Document.<?""Choose a document"", Document>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Get a document form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""Document.<?""Choose a document"", Document>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form."">"", FormParameters);
"}
},
{0,
{"Document walk-through",0,0,"","Select = Documents.<?"""", Document>.Select();

While Selection.Next() Do

	<?>

EndDo;"}
},
{0,
{"RegisterRecords",0,0,"","RegisterRecords.<?""Choose a register"", MetadataObject, ""InformationRegister"", ""AccumulationRegister"", ""AccountingRegister"", ""CalculationRegister"">"}
}
},
{4,
{"Reports",1,0,"",""},
{0,
{"Open a report form",0,0,"Open[Form]","OpenForm(""Report.<?""Choose a report"", Report>.<?""Choose form"", VariantChoice, ""Form"", ""Form"", ""SettingsForm"", ""SettingsForm"", ""VariantForm"", ""VariantForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Open a report form (with parameters)",0,0,"Open[Form]","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""Report.<?""Choose a report"", Report>.<?""Choose form"", VariantChoice, ""Form"", ""Form"", ""SettingsForm"", ""SettingsForm"", ""VariantForm"", ""VariantForm"", ""Generic"", ""Form."">"", FormParameters);"}
},
{0,
{"Get a report form",0,0,"Get[Form]","GetForm(""Report.<?""Choose a report"", Report>.<?""Choose form"", VariantChoice, ""Form"", ""Form"", ""SettingsForm"", ""SettingsForm"", ""VariantForm"", ""VariantForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Get a report form (with parameters)",0,0,"Get[Form]","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""Report.<?""Choose a report"", Report>.<?""Choose form"", VariantChoice, ""Form"", ""Form"", ""SettingsForm"", ""SettingsForm"", ""VariantForm"", ""VariantForm"", ""Generic"", ""Form."">"", FormParameters);
"}
}
},
{4,
{"Data processors",1,0,"",""},
{0,
{"Open a data processor form",0,0,"Open[Form]","OpenForm(""DataProcessor.<?""Choose a data processor"", DataProcessor>.<?""Choose form"", VariantChoice, ""Form"", ""Form"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Open a data processor form (with parameters)",0,0,"Open[Form]","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""DataProcessor.<?""Choose обработку"", DataProcessor>.<?""Choose form"", VariantChoice, ""Form"", ""Form"", ""Generic"", ""Form."">"", FormParameters);"}
},
{0,
{"Get a data processor form",0,0,"Get[Form]","GetForm(""DataProcessor.<?""Choose обработку"", DataProcessor>.<?""Choose form"", VariantChoice, ""Form"", ""Form"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Get a data processor form (with parameters)",0,0,"Get[Form]","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""DataProcessor.<?""Choose обработку"", DataProcessor>.<?""Choose form"", VariantChoice, ""Form"", ""Form"", ""Generic"", ""Form."">"", FormParameters);
"}
}
},
{5,
{"Charts of characteristic types",1,0,"",""},
{0,
{"Open a chart of characteristic types form",0,0,"Open[Form]","OpenForm(""ChartOfCharacteristicTypes.<?""Choose a chart of charateristic types"", ChartOfCharacteristicTypes>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Group form"", ""FolderForm"", ""Group choice form"", ""FolderChoiceForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Open a chart of characteristic types form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""ChartOfCharacteristicTypes.<?""Choose a chart of characteristic types"", ChartOfCharacteristicTypes>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Group form"", ""FolderForm"", ""Group choice form"", ""FolderChoiceForm"", ""Generic"", ""Form."">"", FormParameters);"}
},
{0,
{"Get a chart of characteristic types form",0,0,"Get[Form]","GetForm(""ChartOfCharacteristicTypes.<?""Choose a chart of characteristic types"", ChartOfCharacteristicTypes>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Group form"", ""FolderForm"", ""Group choice form"", ""FolderChoiceForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Get a chart of characteristic types form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""ChartOfCharacteristicTypes.<?""Choose a chart of characteristic types"", ChartOfCharacteristicTypes>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Group form"", ""FolderForm"", ""Group choice form"", ""FolderChoiceForm"", ""Generic"", ""Form."">"", FormParameters);
"}
},
{0,
{"Charts of characteristic types traversal",0,0,"","Selection = ChartOfAccounts.<?"""", ChartOfCharacteristicTypes>.Choose();

While Selection.Next() Do

	<?>

EndDo;"}
}
},
{5,
{"Charts of accounts",1,0,"",""},
{0,
{"Open a chart of accounts form",0,0,"Open[Form]","OpenForm(""ChartOfAccounts.<?""Choose a chart of accounts"", ChartOfAccounts>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Open a chart of accounts form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""ChartOfAccounts.<?""Choose a chart of accounts"", ChartOfAccounts>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form."">"", FormParameters);"}
},
{0,
{"Get a chart of accounts form",0,0,"Get[Form]","GetForm(""ChartOfAccounts.<?""Choose a chart of accounts"", ChartOfAccounts>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Get a chart of accounts form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""ChartOfAccounts.<?""Choose a chart of accounts"", ChartOfAccounts>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form."">"", FormParameters);
"}
},
{0,
{"Find by code",0,0,"","ChartsOfAccounts.<?"""", ChartOfAccounts>.FindByCode(<?>)"}
}
},
{5,
{"Chart of calculation types",1,0,"",""},
{0,
{"Open a chart of calculation types form",0,0,"Open[Form]","OpenForm(""ChartOfCalculationTypes.<?""Choose a chart of calculation types"", ChartOfCalculationTypes>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Open a chart of calculation types form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""ChartOfCalculationTypes.<?""Choose a chart of calculation types"", ChartOfCalculationTypes>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form."">"", FormParameters);"}
},
{0,
{"Get a chart of calculation types form",0,0,"Get[Form]","GetForm(""ChartOfCalculationTypes.<?""Choose a chart of calculation types"", ChartOfCalculationTypes>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Get a chart of calculation types form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""ChartOfCalculationTypes.<?""Choose a chart of calculation types"", ChartOfCalculationTypes>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form."">"", FormParameters);
"}
},
{0,
{"Charts of calculation types traversal",0,0,"","Selection = ChartsOfCalculationTypes.<?"""", ChartOfCalculationTypes>.Choose();

While Selection.Next() Do

	<?>

EndDo;"}
}
},
{5,
{"Business processes",1,0,"",""},
{0,
{"Open a business process form",0,0,"Open[Form]","OpenForm(""BusinessProcess.<?""Choose a business process"", BusinessProcess>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Open a business process form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""BusinessProcess.<?""Choose a business process"", BusinessProcess>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form."">"", FormParameters);"}
},
{0,
{"Get a business process form",0,0,"Get[Form]","GetForm(""BusinessProcess.<?""Choose a business process"", BusinessProcess>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Get a business process form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""BusinessProcess.<?""Choose a business process"", BusinessProcess>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form."">"", FormParameters);
"}
},
{0,
{"Business processes traversal",0,0,"","Selection = BusinessProcessы.<?"""", BusinessProcess>.Choose();

While Selection.Next() Do

	<?>

EndDo;"}
}
},
{4,
{"Tasks",1,0,"",""},
{0,
{"Open a task form",0,0,"Open[Form]","OpenForm(""Task.<?""Choose a task"", Task>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Open a task form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""Task.<?""Choose a task"", Task>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form."">"", FormParameters);"}
},
{0,
{"Get a task form",0,0,"Get[Form]","GetForm(""Task.<?""Choose a task"", Task>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Get a task form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""Task.<?""Choose a task"", Task>.<?""Choose form"", VariantChoice, ""Item form"", ""ObjectForm"", ""List form"", ""ListForm"", ""Choice form"", ""ChoiceForm"", ""Generic"", ""Form."">"", FormParameters);
"}
}
},
{6,
{"Information registers",1,0,"",""},
{0,
{"Open an information register form",0,0,"Open[Form]","OpenForm(""InformationRegister.<?""Choose an information register"", InformationRegister>.<?""Choose form"", VariantChoice, ""Record form"", ""RecordForm"", ""List form"", ""ListForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Open an information register form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""InformationRegister.<?""Choose an information register"", InformationRegister>.<?""Choose form"", VariantChoice, ""Record form"", ""RecordForm"", ""List form"", ""ListForm"", ""Generic"", ""Form."">"", FormParameters);"}
},
{0,
{"Get an information register form",0,0,"Get[Form]","GetForm(""InformationRegister.<?""Choose an information register"", InformationRegister>.<?""Choose form"", VariantChoice, ""Record form"", ""RecordForm"", ""List form"", ""ListForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Get an information register form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""InformationRegister.<?""Choose an information register"", InformationRegister>.<?""Choose form"", VariantChoice, ""Record form"", ""RecordForm"", ""List form"", ""ListForm"", ""Generic"", ""Form."">"", FormParameters);
"}
},
{0,
{"Selection of information register records",0,0,"","Selection = InformationRegister.<?""Choose an information register"", InformationRegister>.Choose();

While Selection.Next() Do

	<?>

EndDo;"}
},
{0,
{"Selection of information register records (by recorder)",0,0,"","Selection = InformationRegister.<?""Choose an information register"", InformationRegister>.ВыбратьПоРегистратору(<?>);

While Selection.Next() Do


EndDo;"}
}
},
{6,
{"Accumulation registers",1,0,"",""},
{0,
{"Open an accumulation register form",0,0,"Open[Form]","OpenForm(""AccumulationRegister.<?""Choose an accumulation register"", AccumulationRegister>.<?""Choose form"", VariantChoice, ""List form"", ""ListForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Open an accumulation register form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""AccumulationRegister.<?""Choose an accumulation register"", AccumulationRegister>.<?""Choose form"", VariantChoice, ""List form"", ""ListForm"", ""Generic"", ""Form."">"", FormParameters);"}
},
{0,
{"Get an accumulation register form",0,0,"Get[Form]","GetForm(""AccumulationRegister.<?""Choose an accumulation register"", AccumulationRegister>.<?""Choose form"", VariantChoice, ""List form"", ""ListForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Get an accumulation register form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""AccumulationRegister.<?""Choose an accumulation register"", AccumulationRegister>.<?""Choose form"", VariantChoice, ""List form"", ""ListForm"", ""Generic"", ""Form."">"", FormParameters);
"}
},
{0,
{"Selection of accumulation register records",0,0,"","Selection = InformationRegister.<?""Choose an accumulation register"", AccumulationRegister>.Choose();

While Selection.Next() Do

	<?>

EndDo;"}
},
{0,
{"Selection of accumulation register records (by recorder)",0,0,"","Selection = InformationRegister.<?""Choose an accumulation register"", AccumulationRegister>.ВыбратьПоРегистратору(<?>);

While Selection.Next() Do


EndDo;"}
}
},
{6,
{"Accounting registers",1,0,"",""},
{0,
{"Open an accounting register form",0,0,"Open[Form]","OpenForm(""AccountingRegister.<?""Choose an accounting register"", AccountingRegister>.<?""Choose form"", VariantChoice, ""List form"", ""ListForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Open an accounting register form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""AccountingRegister.<?""Choose an accounting register"", AccountingRegister>.<?""Choose form"", VariantChoice, ""List form"", ""ListForm"", ""Generic"", ""Form."">"", FormParameters);"}
},
{0,
{"Get an accounting register form",0,0,"Get[Form]","GetForm(""AccountingRegister.<?""Choose an accounting register"", AccountingRegister>.<?""Choose form"", VariantChoice, ""List form"", ""ListForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Get an accounting register form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""AccountingRegister.<?""Choose an accounting register"", AccountingRegister>.<?""Choose form"", VariantChoice, ""List form"", ""ListForm"", ""Generic"", ""Form."">"", FormParameters);
"}
},
{0,
{"Selection of accounting register records",0,0,"","Selection = InformationRegister.<?""Choose an accounting register"", AccountingRegister>.Choose();

While Selection.Next() Do

	<?>

EndDo;"}
},
{0,
{"Selection of accounting register records (by recorder)",0,0,"","Selection = InformationRegister.<?""Choose an accounting register"", AccountingRegister>.ВыбратьПоРегистратору(<?>);

While Selection.Next() Do


EndDo;"}
}
},
{6,
{"Calculation registers",1,0,"",""},
{0,
{"Open a calculation register form",0,0,"Open[Form]","OpenForm(""CalculationRegister.<?""Choose a calculation register"", CalculationRegister>.<?""Choose form"", VariantChoice, ""List form"", ""ListForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Open a calculation register form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
OpenForm(""CalculationRegister.<?""Choose a calculation register"", CalculationRegister>.<?""Choose form"", VariantChoice, ""List form"", ""ListForm"", ""Generic"", ""Form."">"", FormParameters);"}
},
{0,
{"Get a calculation register form",0,0,"Get[Form]","GetForm(""CalculationRegister.<?""Choose a calculation register"", CalculationRegister>.<?""Choose form"", VariantChoice, ""List form"", ""ListForm"", ""Generic"", ""Form.""><?>"");"}
},
{0,
{"Get a calculation register form (with parameters)",0,0,"","FormParameters = New Structure;
FormParameters.Insert(""<?>"", );
Form = GetForm(""CalculationRegister.<?""Choose a calculation register"", CalculationRegister>.<?""Choose form"", VariantChoice, ""List form"", ""ListForm"", ""Generic"", ""Form."">"", FormParameters);
"}
},
{0,
{"Selection of calculation register records",0,0,"","Selection = InformationRegister.<?""Choose a calculation register"", CalculationRegister>.Choose();

While Selection.Next() Do

	<?>

EndDo;"}
},
{0,
{"Selection of calculation register records (by recorder)",0,0,"","Selection = InformationRegister.<?""Choose a calculation register"", CalculationRegister>.ВыбратьПоРегистратору(<?>);

While Selection.Next() Do


EndDo;"}
}
}
},
{11,
{"Other",1,0,"",""},
{0,
{"Message",0,1,"Mes[sage]","Message = New UserMessage;
Message.Text = ""<?>"";
Message.Field = """";
Message.SetData();
Message.Message();"}
},
{0,
{"DoMessageBox",0,0,"DoMes[sageBox]","DoMessageBox(<?>);"}
},
{0,
{"Format",0,0,"Format","Format(<?>, ""<?, FormatString>"")"}
},
{0,
{"Format string",0,1,"","""<?, FormatString>"""}
},
{0,
{"Create a structure",0,0,"Struc[ture]","New Structure(""<?>"", )"}
},
{0,
{"Query",0,0,"","Query = New Query;
Query.Text = ""<?"""", QueryText>"";

Result = Query.Execute();
Selection = Result.Choose();

While Selection.Next() Do



EndDo;
"}
},
{0,
{"Query with parameter",0,0,"","Query = New Query;
Query.Text = ""<?"""", QueryText>"";

Query.SetParameter(""<?>"", );

Result = Query.Execute();
Selection = Result.Choose();

While Selection.Next() Do

	

EndDo;"}
},
{0,
{"Promt",0,0,"DoQuer[yBox]","DoQueryBox(""<?""Prompt text"">"", <?""Dialog Prompt"", VariantChoice, ""YesNo"", ""QuestionDialogMode.YesNo"", ""YesNoCancel"", ""QuestionDialogMode.YesNoCancel"", ""OK"", ""QuestionDialogMode.OK"", ""OKCancel"", ""QuestionDialogMode.OKCancel"", ""RetryCancel"", ""QuestionDialogMode.RetryCancel"", ""AbortRetryIgnore"", ""QuestionDialogMode.AbortRetryIgnore"">)"}
},
{0,
{"Conditional Prompt",0,0,"DoQuer[yBox]","DoQueryBox(""<?""Prompt text"">"", <?""Dialog prompt"", VariantChoice, ""YesNo"", ""QuestionDialogMode.YesNo"", ""YesNoCancel"", ""QuestionDialogMode.YesNoCancel"", ""ОК"", ""QuestionDialogMode.OK"", ""OKCancel"", ""QuestionDialogMode.OKCancel"", ""RetryCancel"", ""QuestionDialogMode.RetryCancel"", ""AbortRetryIgnore"", ""QuestionDialogMode.AbortRetryIgnore"">) = <?""Код возврата диалога"", VariantChoice, ""Yes"", ""DialogReturnCode.Yes"", ""No"", ""DialogReturnCode.No"", ""OK"", ""DialogReturnCode.OK"", ""Cancel"", ""DialogReturnCode.Cancel"", ""Retry"", ""DialogReturnCode.Retry"", ""Abort"", ""DialogReturnCode.Abort"", ""Ignore"", ""DialogReturnCode.Ignore"", ""Timeout"", ""DialogReturnCode.Timeout"">"}
},
{0,
{"Type check",0,0,"","If TypeOf(<?""Expression for type check"">) = Type(""<?""Choose type"", TypeChoice>"") Then

	<?>

EndIf;
"}
},
{0,
{"TypeDescriptionConstructor",0,0,"","<?""Type description constructor"", TypeDescriptionConstructor>"}
}
}
}
}