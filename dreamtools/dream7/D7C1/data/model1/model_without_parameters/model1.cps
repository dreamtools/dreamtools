<?xml version="1.0" encoding="UTF-8"?>
<!-- generated with COPASI 4.8 (Build 35) (http://www.copasi.org) at 2012-05-16 16:42:43 UTC -->
<?oxygen RNGSchema="http://www.copasi.org/static/schema/CopasiML.rng" type="xml"?>
<COPASI xmlns="http://www.copasi.org/static/schema" versionMajor="1" versionMinor="0" versionDevel="35">
  <ListOfFunctions>
    <Function key="Function_39" name="function_4_v9_v1" type="UserDefined" reversible="false">
      <Expression>
        pro8_strength*g8/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_246" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_258" name="g8" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_265" name="pro8_strength" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_45" name="function_4_v9_v2" type="UserDefined" reversible="false">
      <Expression>
        v9_mrna_degradation_rate*v9_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_269" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_270" name="v9_mrna" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_271" name="v9_mrna_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_46" name="function_4_v9_v3" type="UserDefined" reversible="false">
      <Expression>
        rbs9_strength*v9_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_275" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_276" name="rbs9_strength" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_277" name="v9_mrna" order="2" role="modifier"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_47" name="function_4_v9_v4" type="UserDefined" reversible="false">
      <Expression>
        p9_degradation_rate*p9/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_281" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_282" name="p9" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_283" name="p9_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_48" name="function_4_v8_v1" type="UserDefined" reversible="false">
      <Expression>
        pro9_strength*g7/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_287" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_288" name="g7" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_289" name="pro9_strength" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_49" name="function_4_v8_v2" type="UserDefined" reversible="false">
      <Expression>
        v8_mrna_degradation_rate*v8_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_293" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_294" name="v8_mrna" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_295" name="v8_mrna_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_50" name="function_4_v8_v3" type="UserDefined" reversible="false">
      <Expression>
        rbs7_strength*v8_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_299" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_300" name="rbs7_strength" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_301" name="v8_mrna" order="2" role="modifier"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_51" name="function_4_v8_v4" type="UserDefined" reversible="false">
      <Expression>
        p8_degradation_rate*p8/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_305" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_306" name="p8" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_307" name="p8_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_52" name="function_4_v7_v1" type="UserDefined" reversible="false">
      <Expression>
        pro7_strength*g9/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_311" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_312" name="g9" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_313" name="pro7_strength" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_53" name="function_4_v7_v2" type="UserDefined" reversible="false">
      <Expression>
        v7_mrna_degradation_rate*v7_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_317" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_318" name="v7_mrna" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_319" name="v7_mrna_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_54" name="function_4_v7_v3" type="UserDefined" reversible="false">
      <Expression>
        rbs8_strength*v7_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_323" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_324" name="rbs8_strength" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_325" name="v7_mrna" order="2" role="modifier"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_55" name="function_4_v7_v4" type="UserDefined" reversible="false">
      <Expression>
        p7_degradation_rate*p7/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_329" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_330" name="p7" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_331" name="p7_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_56" name="function_4_v6_v1" type="UserDefined" reversible="false">
      <Expression>
        pro6_strength*g6/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_335" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_336" name="g6" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_337" name="pro6_strength" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_57" name="function_4_v6_v2" type="UserDefined" reversible="false">
      <Expression>
        v6_mrna_degradation_rate*v6_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_341" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_342" name="v6_mrna" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_343" name="v6_mrna_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_58" name="function_4_v6_v3" type="UserDefined" reversible="false">
      <Expression>
        rbs6_strength*v6_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_347" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_348" name="rbs6_strength" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_349" name="v6_mrna" order="2" role="modifier"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_59" name="function_4_v6_v4" type="UserDefined" reversible="false">
      <Expression>
        p6_degradation_rate*p6/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_353" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_354" name="p6" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_355" name="p6_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_60" name="function_4_v5_v1" type="UserDefined" reversible="false">
      <Expression>
        pro5_strength*g5/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_359" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_360" name="g5" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_361" name="pro5_strength" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_61" name="function_4_v5_v2" type="UserDefined" reversible="false">
      <Expression>
        v5_mrna_degradation_rate*v5_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_365" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_366" name="v5_mrna" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_367" name="v5_mrna_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_62" name="function_4_v5_v3" type="UserDefined" reversible="false">
      <Expression>
        rbs5_strength*v5_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_371" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_372" name="rbs5_strength" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_373" name="v5_mrna" order="2" role="modifier"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_63" name="function_4_v5_v4" type="UserDefined" reversible="false">
      <Expression>
        p5_degradation_rate*p5/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_377" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_378" name="p5" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_379" name="p5_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_64" name="function_4_v4_v1" type="UserDefined" reversible="false">
      <Expression>
        pro4_strength*g4/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_383" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_384" name="g4" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_385" name="pro4_strength" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_65" name="function_4_v4_v2" type="UserDefined" reversible="false">
      <Expression>
        v4_mrna_degradation_rate*v4_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_389" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_390" name="v4_mrna" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_391" name="v4_mrna_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_66" name="function_4_v4_v3" type="UserDefined" reversible="false">
      <Expression>
        rbs4_strength*v4_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_395" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_396" name="rbs4_strength" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_397" name="v4_mrna" order="2" role="modifier"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_67" name="function_4_v4_v4" type="UserDefined" reversible="false">
      <Expression>
        p4_degradation_rate*p4/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_401" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_402" name="p4" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_403" name="p4_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_68" name="function_4_v3_v1" type="UserDefined" reversible="false">
      <Expression>
        pro3_strength*g3/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_407" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_408" name="g3" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_409" name="pro3_strength" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_69" name="function_4_v3_v2" type="UserDefined" reversible="false">
      <Expression>
        v3_mrna_degradation_rate*v3_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_413" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_414" name="v3_mrna" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_415" name="v3_mrna_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_70" name="function_4_v3_v3" type="UserDefined" reversible="false">
      <Expression>
        rbs3_strength*v3_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_419" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_420" name="rbs3_strength" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_421" name="v3_mrna" order="2" role="modifier"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_71" name="function_4_v3_v4" type="UserDefined" reversible="false">
      <Expression>
        p3_degradation_rate*p3/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_425" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_426" name="p3" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_427" name="p3_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_72" name="function_4_v2_v1" type="UserDefined" reversible="false">
      <Expression>
        pro2_strength*g2/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_431" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_432" name="g2" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_433" name="pro2_strength" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_73" name="function_4_v2_v2" type="UserDefined" reversible="false">
      <Expression>
        v2_mrna_degradation_rate*v2_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_437" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_438" name="v2_mrna" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_439" name="v2_mrna_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_74" name="function_4_v2_v3" type="UserDefined" reversible="false">
      <Expression>
        rbs2_strength*v2_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_443" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_444" name="rbs2_strength" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_445" name="v2_mrna" order="2" role="modifier"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_75" name="function_4_v2_v4" type="UserDefined" reversible="false">
      <Expression>
        p2_degradation_rate*p2/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_449" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_450" name="p2" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_451" name="p2_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_76" name="function_4_v1_v1" type="UserDefined" reversible="false">
      <Expression>
        pro1_strength*g1/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_455" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_456" name="g1" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_457" name="pro1_strength" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_77" name="function_4_v1_v2" type="UserDefined" reversible="false">
      <Expression>
        v1_mrna_degradation_rate*v1_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_461" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_462" name="v1_mrna" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_463" name="v1_mrna_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_78" name="function_4_v1_v3" type="UserDefined" reversible="false">
      <Expression>
        rbs1_strength*v1_mrna/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_467" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_468" name="rbs1_strength" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_469" name="v1_mrna" order="2" role="modifier"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_79" name="function_4_v1_v4" type="UserDefined" reversible="false">
      <Expression>
        p1_degradation_rate*p1/DefaultCompartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_473" name="DefaultCompartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_474" name="p1" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_475" name="p1_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
  </ListOfFunctions>
  <Model key="Model_0" name="*model_9_genes.tic" simulationType="time" timeUnit="s" volumeUnit="l" areaUnit="m²" lengthUnit="m" quantityUnit="mol" type="deterministic" avogadroConstant="6.02214179e+023">
    <MiriamAnnotation>
<rdf:RDF
   xmlns:dcterms="http://purl.org/dc/terms/"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Model_0">
    <dcterms:created>
      <rdf:Description>
        <dcterms:W3CDTF>2012-05-16T09:42:25Z</dcterms:W3CDTF>
      </rdf:Description>
    </dcterms:created>
  </rdf:Description>
</rdf:RDF>

    </MiriamAnnotation>
    <ListOfCompartments>
      <Compartment key="Compartment_0" name="DefaultCompartment" simulationType="fixed" dimensionality="3">
      </Compartment>
    </ListOfCompartments>
    <ListOfMetabolites>
      <Metabolite key="Metabolite_0" name="as1" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          (1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p1],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r1_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r1_h],Reference=Value&gt;-1)/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p1],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r1_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r1_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_1" name="as2" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          (1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p1],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r2_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r2_h],Reference=Value&gt;-1)/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p1],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r2_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r2_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_2" name="as3" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          (1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p4],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r5_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r5_h],Reference=Value&gt;-1)/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p4],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r5_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r5_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_3" name="as5" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          (1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p8],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r13_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r13_h],Reference=Value&gt;-1)/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p8],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r13_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r13_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_4" name="as6" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          (1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p9],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r9_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r9_h],Reference=Value&gt;-1)/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p9],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r9_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r9_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_5" name="as7" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          (1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p6],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r12_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r12_h],Reference=Value&gt;-1)/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p6],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r12_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r12_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_6" name="as9" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          (1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p6],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r11_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r11_h],Reference=Value&gt;-1)/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p6],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r11_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r11_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_7" name="g1" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          (1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p1],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r1_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r1_h],Reference=Value&gt;-1)/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p1],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r1_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r1_h],Reference=Value&gt;)*(1/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p2],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r4_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r4_h],Reference=Value&gt;)*1/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p6],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r8_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r8_h],Reference=Value&gt;))
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_8" name="g2" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          (1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p1],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r2_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r2_h],Reference=Value&gt;-1)/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p1],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r2_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r2_h],Reference=Value&gt;)*(1/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p3],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r3_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r3_h],Reference=Value&gt;))
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_9" name="g3" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          (1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p4],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r5_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r5_h],Reference=Value&gt;-1)/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p4],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r5_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r5_h],Reference=Value&gt;)*(1/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p5],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r7_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r7_h],Reference=Value&gt;))
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_10" name="g4" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          (1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p9],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r9_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r9_h],Reference=Value&gt;-1)/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p9],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r9_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r9_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_11" name="g5" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          (1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p8],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r13_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r13_h],Reference=Value&gt;-1)/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p8],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r13_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r13_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_12" name="g6" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_13" name="g7" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          (1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p6],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r12_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r12_h],Reference=Value&gt;-1)/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p6],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r12_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r12_h],Reference=Value&gt;)*(1/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p7],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r6_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r6_h],Reference=Value&gt;))
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_14" name="g8" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          1/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p9],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r10_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r10_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_15" name="g9" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          (1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p6],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r11_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r11_h],Reference=Value&gt;-1)/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p6],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r11_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r11_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_16" name="p1" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_17" name="p2" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_18" name="p3" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_19" name="p4" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_20" name="p5" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_21" name="p6" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_22" name="p7" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_23" name="p8" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_24" name="p9" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_25" name="pro1" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_26" name="pro2" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_27" name="pro3" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_28" name="pro4" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_29" name="pro5" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_30" name="pro6" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_31" name="pro7" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_32" name="pro8" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_33" name="pro9" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_34" name="rbs1" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_35" name="rbs2" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_36" name="rbs3" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_37" name="rbs4" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_38" name="rbs5" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_39" name="rbs6" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_40" name="rbs7" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_41" name="rbs8" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_42" name="rbs9" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_43" name="rs1a" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          1/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p2],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r4_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r4_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_44" name="rs1b" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          1/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p6],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r8_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r8_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_45" name="rs2" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          1/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p3],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r3_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r3_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_46" name="rs3" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          1/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p5],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r7_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r7_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_47" name="rs7" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          1/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p7],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r6_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r6_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_48" name="rs8" simulationType="assignment" compartment="Compartment_0">
        <Expression>
          1/(1+(&lt;CN=Root,Model=*model_9_genes.tic,Vector=Compartments[DefaultCompartment],Vector=Metabolites[p9],Reference=Concentration&gt;/&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r10_Kd],Reference=Value&gt;)^&lt;CN=Root,Model=*model_9_genes.tic,Vector=Values[r10_h],Reference=Value&gt;)
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_49" name="v1_mrna" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_50" name="v2_mrna" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_51" name="v3_mrna" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_52" name="v4_mrna" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_53" name="v5_mrna" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_54" name="v6_mrna" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_55" name="v7_mrna" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_56" name="v8_mrna" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_57" name="v9_mrna" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
    </ListOfMetabolites>
    <ListOfModelValues>
      <ModelValue key="ModelValue_0" name="v8_mrna_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_1" name="v9_mrna_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_2" name="p1_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_3" name="p2_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_4" name="p3_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_5" name="p4_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_6" name="p5_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_7" name="p6_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_8" name="p7_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_9" name="p8_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_10" name="p9_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_11" name="r1_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_12" name="r1_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_13" name="r2_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_14" name="r2_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_15" name="r3_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_16" name="r3_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_17" name="r4_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_18" name="r4_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_19" name="r5_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_20" name="r5_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_21" name="r6_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_22" name="r6_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_23" name="r7_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_24" name="r7_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_25" name="r8_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_26" name="r8_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_27" name="r9_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_28" name="r9_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_29" name="v1_mrna_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_30" name="v2_mrna_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_31" name="pro1_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_32" name="pro2_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_33" name="pro3_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_34" name="pro4_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_35" name="pro5_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_36" name="v3_mrna_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_37" name="pro6_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_38" name="pro7_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_39" name="pro8_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_40" name="pro9_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_41" name="v4_mrna_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_42" name="r10_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_43" name="r10_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_44" name="r11_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_45" name="r11_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_46" name="r12_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_47" name="r12_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_48" name="r13_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_49" name="r13_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_50" name="v5_mrna_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_51" name="rbs1_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_52" name="rbs2_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_53" name="rbs3_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_54" name="rbs4_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_55" name="rbs5_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_56" name="v6_mrna_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_57" name="rbs6_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_58" name="rbs7_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_59" name="rbs8_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_60" name="rbs9_strength" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_61" name="v7_mrna_degradation_rate" simulationType="fixed">
      </ModelValue>
    </ListOfModelValues>
    <ListOfReactions>
      <Reaction key="Reaction_0" name="v9_v1" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_57" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_14" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1631" name="pro8_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_39">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_246">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_258">
              <SourceParameter reference="Metabolite_14"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_265">
              <SourceParameter reference="ModelValue_39"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_1" name="v9_v2" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_57" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1632" name="v9_mrna_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_45">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_269">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_270">
              <SourceParameter reference="Metabolite_57"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_271">
              <SourceParameter reference="ModelValue_1"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_2" name="v9_v3" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_24" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_57" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1633" name="rbs9_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_46">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_275">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_276">
              <SourceParameter reference="ModelValue_60"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_277">
              <SourceParameter reference="Metabolite_57"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_3" name="v9_v4" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_24" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1636" name="p9_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_47">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_281">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_282">
              <SourceParameter reference="Metabolite_24"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_283">
              <SourceParameter reference="ModelValue_10"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_4" name="v8_v1" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_56" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_13" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1635" name="pro9_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_48">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_287">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_288">
              <SourceParameter reference="Metabolite_13"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_289">
              <SourceParameter reference="ModelValue_40"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_5" name="v8_v2" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_56" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1637" name="v8_mrna_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_49">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_293">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_294">
              <SourceParameter reference="Metabolite_56"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_295">
              <SourceParameter reference="ModelValue_0"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_6" name="v8_v3" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_23" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_56" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1634" name="rbs7_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_50">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_299">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_300">
              <SourceParameter reference="ModelValue_58"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_301">
              <SourceParameter reference="Metabolite_56"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_7" name="v8_v4" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_23" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1638" name="p8_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_51">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_305">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_306">
              <SourceParameter reference="Metabolite_23"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_307">
              <SourceParameter reference="ModelValue_9"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_8" name="v7_v1" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_55" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_15" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1639" name="pro7_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_52">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_311">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_312">
              <SourceParameter reference="Metabolite_15"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_313">
              <SourceParameter reference="ModelValue_38"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_9" name="v7_v2" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_55" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1640" name="v7_mrna_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_53">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_317">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_318">
              <SourceParameter reference="Metabolite_55"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_319">
              <SourceParameter reference="ModelValue_61"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_10" name="v7_v3" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_22" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_55" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1641" name="rbs8_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_54">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_323">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_324">
              <SourceParameter reference="ModelValue_59"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_325">
              <SourceParameter reference="Metabolite_55"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_11" name="v7_v4" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_22" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1642" name="p7_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_55">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_329">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_330">
              <SourceParameter reference="Metabolite_22"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_331">
              <SourceParameter reference="ModelValue_8"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_12" name="v6_v1" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_54" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1643" name="pro6_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_56">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_335">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_336">
              <SourceParameter reference="Metabolite_12"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_337">
              <SourceParameter reference="ModelValue_37"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_13" name="v6_v2" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_54" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1644" name="v6_mrna_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_57">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_341">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_342">
              <SourceParameter reference="Metabolite_54"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_343">
              <SourceParameter reference="ModelValue_56"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_14" name="v6_v3" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_21" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_54" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1645" name="rbs6_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_58">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_347">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_348">
              <SourceParameter reference="ModelValue_57"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_349">
              <SourceParameter reference="Metabolite_54"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_15" name="v6_v4" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_21" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1646" name="p6_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_59">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_353">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_354">
              <SourceParameter reference="Metabolite_21"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_355">
              <SourceParameter reference="ModelValue_7"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_16" name="v5_v1" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_53" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1647" name="pro5_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_60">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_359">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_360">
              <SourceParameter reference="Metabolite_11"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_361">
              <SourceParameter reference="ModelValue_35"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_17" name="v5_v2" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_53" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1648" name="v5_mrna_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_61">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_365">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_366">
              <SourceParameter reference="Metabolite_53"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_367">
              <SourceParameter reference="ModelValue_50"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_18" name="v5_v3" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_20" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_53" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1649" name="rbs5_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_62">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_371">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_372">
              <SourceParameter reference="ModelValue_55"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_373">
              <SourceParameter reference="Metabolite_53"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_19" name="v5_v4" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_20" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1650" name="p5_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_63">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_377">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_378">
              <SourceParameter reference="Metabolite_20"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_379">
              <SourceParameter reference="ModelValue_6"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_20" name="v4_v1" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_52" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_10" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1651" name="pro4_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_64">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_383">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_384">
              <SourceParameter reference="Metabolite_10"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_385">
              <SourceParameter reference="ModelValue_34"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_21" name="v4_v2" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_52" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1652" name="v4_mrna_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_65">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_389">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_390">
              <SourceParameter reference="Metabolite_52"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_391">
              <SourceParameter reference="ModelValue_41"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_22" name="v4_v3" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_19" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_52" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1653" name="rbs4_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_66">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_395">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_396">
              <SourceParameter reference="ModelValue_54"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_397">
              <SourceParameter reference="Metabolite_52"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_23" name="v4_v4" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_19" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1656" name="p4_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_67">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_401">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_402">
              <SourceParameter reference="Metabolite_19"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_403">
              <SourceParameter reference="ModelValue_5"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_24" name="v3_v1" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_51" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_9" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1655" name="pro3_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_68">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_407">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_408">
              <SourceParameter reference="Metabolite_9"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_409">
              <SourceParameter reference="ModelValue_33"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_25" name="v3_v2" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_51" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1654" name="v3_mrna_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_69">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_413">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_414">
              <SourceParameter reference="Metabolite_51"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_415">
              <SourceParameter reference="ModelValue_36"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_26" name="v3_v3" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_18" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_51" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1657" name="rbs3_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_70">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_419">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_420">
              <SourceParameter reference="ModelValue_53"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_421">
              <SourceParameter reference="Metabolite_51"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_27" name="v3_v4" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_18" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1658" name="p3_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_71">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_425">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_426">
              <SourceParameter reference="Metabolite_18"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_427">
              <SourceParameter reference="ModelValue_4"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_28" name="v2_v1" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_50" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_8" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1661" name="pro2_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_72">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_431">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_432">
              <SourceParameter reference="Metabolite_8"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_433">
              <SourceParameter reference="ModelValue_32"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_29" name="v2_v2" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_50" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1660" name="v2_mrna_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_73">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_437">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_438">
              <SourceParameter reference="Metabolite_50"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_439">
              <SourceParameter reference="ModelValue_30"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_30" name="v2_v3" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_17" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_50" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1659" name="rbs2_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_74">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_443">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_444">
              <SourceParameter reference="ModelValue_52"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_445">
              <SourceParameter reference="Metabolite_50"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_31" name="v2_v4" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_17" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1662" name="p2_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_75">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_449">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_450">
              <SourceParameter reference="Metabolite_17"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_451">
              <SourceParameter reference="ModelValue_3"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_32" name="v1_v1" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_49" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_7" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1663" name="pro1_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_76">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_455">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_456">
              <SourceParameter reference="Metabolite_7"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_457">
              <SourceParameter reference="ModelValue_31"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_33" name="v1_v2" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_49" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1664" name="v1_mrna_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_77">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_461">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_462">
              <SourceParameter reference="Metabolite_49"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_463">
              <SourceParameter reference="ModelValue_29"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_34" name="v1_v3" reversible="false">
        <ListOfProducts>
          <Product metabolite="Metabolite_16" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_49" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1665" name="rbs1_strength" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_78">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_467">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_468">
              <SourceParameter reference="ModelValue_51"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_469">
              <SourceParameter reference="Metabolite_49"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_35" name="v1_v4" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_16" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_1666" name="p1_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_79">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_473">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_474">
              <SourceParameter reference="Metabolite_16"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_475">
              <SourceParameter reference="ModelValue_2"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
    </ListOfReactions>
    <StateTemplate>
      <StateTemplateVariable objectReference="Model_0"/>
      <StateTemplateVariable objectReference="Metabolite_16"/>
      <StateTemplateVariable objectReference="Metabolite_17"/>
      <StateTemplateVariable objectReference="Metabolite_18"/>
      <StateTemplateVariable objectReference="Metabolite_19"/>
      <StateTemplateVariable objectReference="Metabolite_20"/>
      <StateTemplateVariable objectReference="Metabolite_21"/>
      <StateTemplateVariable objectReference="Metabolite_22"/>
      <StateTemplateVariable objectReference="Metabolite_23"/>
      <StateTemplateVariable objectReference="Metabolite_24"/>
      <StateTemplateVariable objectReference="Metabolite_49"/>
      <StateTemplateVariable objectReference="Metabolite_50"/>
      <StateTemplateVariable objectReference="Metabolite_51"/>
      <StateTemplateVariable objectReference="Metabolite_52"/>
      <StateTemplateVariable objectReference="Metabolite_53"/>
      <StateTemplateVariable objectReference="Metabolite_54"/>
      <StateTemplateVariable objectReference="Metabolite_55"/>
      <StateTemplateVariable objectReference="Metabolite_56"/>
      <StateTemplateVariable objectReference="Metabolite_57"/>
      <StateTemplateVariable objectReference="Metabolite_7"/>
      <StateTemplateVariable objectReference="Metabolite_8"/>
      <StateTemplateVariable objectReference="Metabolite_9"/>
      <StateTemplateVariable objectReference="Metabolite_10"/>
      <StateTemplateVariable objectReference="Metabolite_11"/>
      <StateTemplateVariable objectReference="Metabolite_13"/>
      <StateTemplateVariable objectReference="Metabolite_14"/>
      <StateTemplateVariable objectReference="Metabolite_15"/>
      <StateTemplateVariable objectReference="Metabolite_0"/>
      <StateTemplateVariable objectReference="Metabolite_1"/>
      <StateTemplateVariable objectReference="Metabolite_2"/>
      <StateTemplateVariable objectReference="Metabolite_3"/>
      <StateTemplateVariable objectReference="Metabolite_4"/>
      <StateTemplateVariable objectReference="Metabolite_5"/>
      <StateTemplateVariable objectReference="Metabolite_6"/>
      <StateTemplateVariable objectReference="Metabolite_43"/>
      <StateTemplateVariable objectReference="Metabolite_44"/>
      <StateTemplateVariable objectReference="Metabolite_45"/>
      <StateTemplateVariable objectReference="Metabolite_46"/>
      <StateTemplateVariable objectReference="Metabolite_47"/>
      <StateTemplateVariable objectReference="Metabolite_48"/>
      <StateTemplateVariable objectReference="Metabolite_12"/>
      <StateTemplateVariable objectReference="Metabolite_25"/>
      <StateTemplateVariable objectReference="Metabolite_26"/>
      <StateTemplateVariable objectReference="Metabolite_27"/>
      <StateTemplateVariable objectReference="Metabolite_28"/>
      <StateTemplateVariable objectReference="Metabolite_29"/>
      <StateTemplateVariable objectReference="Metabolite_30"/>
      <StateTemplateVariable objectReference="Metabolite_31"/>
      <StateTemplateVariable objectReference="Metabolite_32"/>
      <StateTemplateVariable objectReference="Metabolite_33"/>
      <StateTemplateVariable objectReference="Metabolite_34"/>
      <StateTemplateVariable objectReference="Metabolite_35"/>
      <StateTemplateVariable objectReference="Metabolite_36"/>
      <StateTemplateVariable objectReference="Metabolite_37"/>
      <StateTemplateVariable objectReference="Metabolite_38"/>
      <StateTemplateVariable objectReference="Metabolite_39"/>
      <StateTemplateVariable objectReference="Metabolite_40"/>
      <StateTemplateVariable objectReference="Metabolite_41"/>
      <StateTemplateVariable objectReference="Metabolite_42"/>
      <StateTemplateVariable objectReference="ModelValue_0"/>
      <StateTemplateVariable objectReference="ModelValue_1"/>
      <StateTemplateVariable objectReference="ModelValue_2"/>
      <StateTemplateVariable objectReference="ModelValue_3"/>
      <StateTemplateVariable objectReference="ModelValue_4"/>
      <StateTemplateVariable objectReference="ModelValue_5"/>
      <StateTemplateVariable objectReference="ModelValue_6"/>
      <StateTemplateVariable objectReference="ModelValue_7"/>
      <StateTemplateVariable objectReference="ModelValue_8"/>
      <StateTemplateVariable objectReference="ModelValue_9"/>
      <StateTemplateVariable objectReference="ModelValue_10"/>
      <StateTemplateVariable objectReference="ModelValue_11"/>
      <StateTemplateVariable objectReference="ModelValue_12"/>
      <StateTemplateVariable objectReference="ModelValue_13"/>
      <StateTemplateVariable objectReference="ModelValue_14"/>
      <StateTemplateVariable objectReference="ModelValue_15"/>
      <StateTemplateVariable objectReference="ModelValue_16"/>
      <StateTemplateVariable objectReference="ModelValue_17"/>
      <StateTemplateVariable objectReference="ModelValue_18"/>
      <StateTemplateVariable objectReference="ModelValue_19"/>
      <StateTemplateVariable objectReference="ModelValue_20"/>
      <StateTemplateVariable objectReference="ModelValue_21"/>
      <StateTemplateVariable objectReference="ModelValue_22"/>
      <StateTemplateVariable objectReference="ModelValue_23"/>
      <StateTemplateVariable objectReference="ModelValue_24"/>
      <StateTemplateVariable objectReference="ModelValue_25"/>
      <StateTemplateVariable objectReference="ModelValue_26"/>
      <StateTemplateVariable objectReference="ModelValue_27"/>
      <StateTemplateVariable objectReference="ModelValue_28"/>
      <StateTemplateVariable objectReference="ModelValue_29"/>
      <StateTemplateVariable objectReference="ModelValue_30"/>
      <StateTemplateVariable objectReference="ModelValue_31"/>
      <StateTemplateVariable objectReference="ModelValue_32"/>
      <StateTemplateVariable objectReference="ModelValue_33"/>
      <StateTemplateVariable objectReference="ModelValue_34"/>
      <StateTemplateVariable objectReference="ModelValue_35"/>
      <StateTemplateVariable objectReference="ModelValue_36"/>
      <StateTemplateVariable objectReference="ModelValue_37"/>
      <StateTemplateVariable objectReference="ModelValue_38"/>
      <StateTemplateVariable objectReference="ModelValue_39"/>
      <StateTemplateVariable objectReference="ModelValue_40"/>
      <StateTemplateVariable objectReference="ModelValue_41"/>
      <StateTemplateVariable objectReference="ModelValue_42"/>
      <StateTemplateVariable objectReference="ModelValue_43"/>
      <StateTemplateVariable objectReference="ModelValue_44"/>
      <StateTemplateVariable objectReference="ModelValue_45"/>
      <StateTemplateVariable objectReference="ModelValue_46"/>
      <StateTemplateVariable objectReference="ModelValue_47"/>
      <StateTemplateVariable objectReference="ModelValue_48"/>
      <StateTemplateVariable objectReference="ModelValue_49"/>
      <StateTemplateVariable objectReference="ModelValue_50"/>
      <StateTemplateVariable objectReference="ModelValue_51"/>
      <StateTemplateVariable objectReference="ModelValue_52"/>
      <StateTemplateVariable objectReference="ModelValue_53"/>
      <StateTemplateVariable objectReference="ModelValue_54"/>
      <StateTemplateVariable objectReference="ModelValue_55"/>
      <StateTemplateVariable objectReference="ModelValue_56"/>
      <StateTemplateVariable objectReference="ModelValue_57"/>
      <StateTemplateVariable objectReference="ModelValue_58"/>
      <StateTemplateVariable objectReference="ModelValue_59"/>
      <StateTemplateVariable objectReference="ModelValue_60"/>
      <StateTemplateVariable objectReference="ModelValue_61"/>
      <StateTemplateVariable objectReference="Compartment_0"/>
    </StateTemplate>
    <InitialState type="initialState">
      0 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 0 0 0 0 0 0 0 0 0 7.5276772375e+022 1.5055354475e+023 1.5055354475e+023 3.011070895e+023 3.011070895e+023 1.5055354475e+023 3.011070895e+023 3.011070895e+023 3.011070895e+023 3.011070895e+023 3.011070895e+023 3.011070895e+023 3.011070895e+023 3.011070895e+023 3.011070895e+023 3.011070895e+023 3.011070895e+023 3.011070895e+023 3.011070895e+023 3.011070895e+023 3.011070895e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    </InitialState>
  </Model>
  <ListOfTasks>
    <Task key="Task_10" name="Steady-State" type="steadyState" scheduled="false" updateModel="false">
      <Report reference="Report_7" target="" append="1"/>
      <Problem>
        <Parameter name="JacobianRequested" type="bool" value="1"/>
        <Parameter name="StabilityAnalysisRequested" type="bool" value="1"/>
      </Problem>
      <Method name="Enhanced Newton" type="EnhancedNewton">
        <Parameter name="Resolution" type="unsignedFloat" value="1e-009"/>
        <Parameter name="Derivation Factor" type="unsignedFloat" value="0.001"/>
        <Parameter name="Use Newton" type="bool" value="1"/>
        <Parameter name="Use Integration" type="bool" value="1"/>
        <Parameter name="Use Back Integration" type="bool" value="1"/>
        <Parameter name="Accept Negative Concentrations" type="bool" value="0"/>
        <Parameter name="Iteration Limit" type="unsignedInteger" value="50"/>
        <Parameter name="Maximum duration for forward integration" type="unsignedFloat" value="1000000000"/>
        <Parameter name="Maximum duration for backward integration" type="unsignedFloat" value="1000000"/>
      </Method>
    </Task>
    <Task key="Task_9" name="Time-Course" type="timeCourse" scheduled="false" updateModel="false">
      <Problem>
        <Parameter name="StepNumber" type="unsignedInteger" value="100"/>
        <Parameter name="StepSize" type="float" value="0.01"/>
        <Parameter name="Duration" type="float" value="1"/>
        <Parameter name="TimeSeriesRequested" type="bool" value="1"/>
        <Parameter name="OutputStartTime" type="float" value="0"/>
        <Parameter name="Output Event" type="bool" value="0"/>
      </Problem>
      <Method name="Deterministic (LSODA)" type="Deterministic(LSODA)">
        <Parameter name="Integrate Reduced Model" type="bool" value="0"/>
        <Parameter name="Relative Tolerance" type="unsignedFloat" value="1e-006"/>
        <Parameter name="Absolute Tolerance" type="unsignedFloat" value="1e-012"/>
        <Parameter name="Max Internal Steps" type="unsignedInteger" value="10000"/>
      </Method>
    </Task>
    <Task key="Task_8" name="Scan" type="scan" scheduled="false" updateModel="false">
      <Problem>
        <Parameter name="Subtask" type="unsignedInteger" value="1"/>
        <ParameterGroup name="ScanItems">
        </ParameterGroup>
        <Parameter name="Output in subtask" type="bool" value="1"/>
        <Parameter name="Adjust initial conditions" type="bool" value="0"/>
      </Problem>
      <Method name="Scan Framework" type="ScanFramework">
      </Method>
    </Task>
    <Task key="Task_7" name="Elementary Flux Modes" type="fluxMode" scheduled="false" updateModel="false">
      <Report reference="Report_6" target="" append="1"/>
      <Problem>
      </Problem>
      <Method name="EFM Algorithm" type="EFMAlgorithm">
      </Method>
    </Task>
    <Task key="Task_6" name="Optimization" type="optimization" scheduled="false" updateModel="false">
      <Report reference="Report_5" target="" append="1"/>
      <Problem>
        <Parameter name="Subtask" type="cn" value="CN=Root,Vector=TaskList[Steady-State]"/>
        <ParameterText name="ObjectiveExpression" type="expression">
          
        </ParameterText>
        <Parameter name="Maximize" type="bool" value="0"/>
        <Parameter name="Randomize Start Values" type="bool" value="0"/>
        <Parameter name="Calculate Statistics" type="bool" value="1"/>
        <ParameterGroup name="OptimizationItemList">
        </ParameterGroup>
        <ParameterGroup name="OptimizationConstraintList">
        </ParameterGroup>
      </Problem>
      <Method name="Random Search" type="RandomSearch">
        <Parameter name="Number of Iterations" type="unsignedInteger" value="100000"/>
        <Parameter name="Random Number Generator" type="unsignedInteger" value="1"/>
        <Parameter name="Seed" type="unsignedInteger" value="0"/>
      </Method>
    </Task>
    <Task key="Task_5" name="Parameter Estimation" type="parameterFitting" scheduled="false" updateModel="false">
      <Report reference="Report_4" target="" append="1"/>
      <Problem>
        <Parameter name="Maximize" type="bool" value="0"/>
        <Parameter name="Randomize Start Values" type="bool" value="0"/>
        <Parameter name="Calculate Statistics" type="bool" value="1"/>
        <ParameterGroup name="OptimizationItemList">
        </ParameterGroup>
        <ParameterGroup name="OptimizationConstraintList">
        </ParameterGroup>
        <Parameter name="Steady-State" type="cn" value="CN=Root,Vector=TaskList[Steady-State]"/>
        <Parameter name="Time-Course" type="cn" value="CN=Root,Vector=TaskList[Time-Course]"/>
        <ParameterGroup name="Experiment Set">
        </ParameterGroup>
      </Problem>
      <Method name="Evolutionary Programming" type="EvolutionaryProgram">
        <Parameter name="Number of Generations" type="unsignedInteger" value="200"/>
        <Parameter name="Population Size" type="unsignedInteger" value="20"/>
        <Parameter name="Random Number Generator" type="unsignedInteger" value="1"/>
        <Parameter name="Seed" type="unsignedInteger" value="0"/>
      </Method>
    </Task>
    <Task key="Task_4" name="Metabolic Control Analysis" type="metabolicControlAnalysis" scheduled="false" updateModel="false">
      <Report reference="Report_3" target="" append="1"/>
      <Problem>
        <Parameter name="Steady-State" type="key" value="Task_10"/>
      </Problem>
      <Method name="MCA Method (Reder)" type="MCAMethod(Reder)">
        <Parameter name="Modulation Factor" type="unsignedFloat" value="1e-009"/>
      </Method>
    </Task>
    <Task key="Task_3" name="Lyapunov Exponents" type="lyapunovExponents" scheduled="false" updateModel="false">
      <Report reference="Report_2" target="" append="1"/>
      <Problem>
        <Parameter name="ExponentNumber" type="unsignedInteger" value="3"/>
        <Parameter name="DivergenceRequested" type="bool" value="1"/>
        <Parameter name="TransientTime" type="float" value="0"/>
      </Problem>
      <Method name="Wolf Method" type="WolfMethod">
        <Parameter name="Orthonormalization Interval" type="unsignedFloat" value="1"/>
        <Parameter name="Overall time" type="unsignedFloat" value="1000"/>
        <Parameter name="Relative Tolerance" type="unsignedFloat" value="1e-006"/>
        <Parameter name="Absolute Tolerance" type="unsignedFloat" value="1e-012"/>
        <Parameter name="Max Internal Steps" type="unsignedInteger" value="10000"/>
      </Method>
    </Task>
    <Task key="Task_2" name="Time Scale Separation Analysis" type="timeScaleSeparationAnalysis" scheduled="false" updateModel="false">
      <Report reference="Report_1" target="" append="1"/>
      <Problem>
        <Parameter name="StepNumber" type="unsignedInteger" value="100"/>
        <Parameter name="StepSize" type="float" value="0.01"/>
        <Parameter name="Duration" type="float" value="1"/>
        <Parameter name="TimeSeriesRequested" type="bool" value="1"/>
        <Parameter name="OutputStartTime" type="float" value="0"/>
      </Problem>
      <Method name="ILDM (LSODA,Deuflhard)" type="TimeScaleSeparation(ILDM,Deuflhard)">
        <Parameter name="Deuflhard Tolerance" type="unsignedFloat" value="1e-006"/>
      </Method>
    </Task>
    <Task key="Task_1" name="Sensitivities" type="sensitivities" scheduled="false" updateModel="false">
      <Report reference="Report_0" target="" append="1"/>
      <Problem>
        <Parameter name="SubtaskType" type="unsignedInteger" value="1"/>
        <ParameterGroup name="TargetFunctions">
          <Parameter name="SingleObject" type="cn" value=""/>
          <Parameter name="ObjectListType" type="unsignedInteger" value="7"/>
        </ParameterGroup>
        <ParameterGroup name="ListOfVariables">
          <ParameterGroup name="Variables">
            <Parameter name="SingleObject" type="cn" value=""/>
            <Parameter name="ObjectListType" type="unsignedInteger" value="41"/>
          </ParameterGroup>
        </ParameterGroup>
      </Problem>
      <Method name="Sensitivities Method" type="SensitivitiesMethod">
        <Parameter name="Delta factor" type="unsignedFloat" value="0.001"/>
        <Parameter name="Delta minimum" type="unsignedFloat" value="1e-012"/>
      </Method>
    </Task>
    <Task key="Task_11" name="Moieties" type="moieties" scheduled="false" updateModel="false">
      <Problem>
      </Problem>
      <Method name="Householder Reduction" type="Householder">
      </Method>
    </Task>
  </ListOfTasks>
  <ListOfReports>
    <Report key="Report_7" name="Steady-State" taskType="steadyState" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Footer>
        <Object cn="CN=Root,Vector=TaskList[Steady-State]"/>
      </Footer>
    </Report>
    <Report key="Report_6" name="Elementary Flux Modes" taskType="fluxMode" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Footer>
        <Object cn="CN=Root,Vector=TaskList[Elementary Flux Modes],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_5" name="Optimization" taskType="optimization" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Object=Description"/>
        <Object cn="String=\[Function Evaluations\]"/>
        <Object cn="Separator=&#x09;"/>
        <Object cn="String=\[Best Value\]"/>
        <Object cn="Separator=&#x09;"/>
        <Object cn="String=\[Best Parameters\]"/>
      </Header>
      <Body>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Problem=Optimization,Reference=Function Evaluations"/>
        <Object cn="Separator=&#x09;"/>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Problem=Optimization,Reference=Best Value"/>
        <Object cn="Separator=&#x09;"/>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Problem=Optimization,Reference=Best Parameters"/>
      </Body>
      <Footer>
        <Object cn="String=&#x0a;"/>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_4" name="Parameter Estimation" taskType="parameterFitting" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Object=Description"/>
        <Object cn="String=\[Function Evaluations\]"/>
        <Object cn="Separator=&#x09;"/>
        <Object cn="String=\[Best Value\]"/>
        <Object cn="Separator=&#x09;"/>
        <Object cn="String=\[Best Parameters\]"/>
      </Header>
      <Body>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Function Evaluations"/>
        <Object cn="Separator=&#x09;"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Best Value"/>
        <Object cn="Separator=&#x09;"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Best Parameters"/>
      </Body>
      <Footer>
        <Object cn="String=&#x0a;"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_3" name="Metabolic Control Analysis" taskType="metabolicControlAnalysis" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Metabolic Control Analysis],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#x0a;"/>
        <Object cn="CN=Root,Vector=TaskList[Metabolic Control Analysis],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_2" name="Lyapunov Exponents" taskType="lyapunovExponents" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Lyapunov Exponents],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#x0a;"/>
        <Object cn="CN=Root,Vector=TaskList[Lyapunov Exponents],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_1" name="Time Scale Separation Analysis" taskType="timeScaleSeparationAnalysis" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Time Scale Separation Analysis],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#x0a;"/>
        <Object cn="CN=Root,Vector=TaskList[Time Scale Separation Analysis],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_0" name="Sensitivities" taskType="sensitivities" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Sensitivities],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#x0a;"/>
        <Object cn="CN=Root,Vector=TaskList[Sensitivities],Object=Result"/>
      </Footer>
    </Report>
  </ListOfReports>
  <GUI>
  </GUI>
  <SBMLReference file="model_9_genes.no_params.sbml">
    <SBMLMap SBMLid="DefaultCompartment" COPASIkey="Compartment_0"/>
    <SBMLMap SBMLid="as1" COPASIkey="Metabolite_0"/>
    <SBMLMap SBMLid="as2" COPASIkey="Metabolite_1"/>
    <SBMLMap SBMLid="as3" COPASIkey="Metabolite_2"/>
    <SBMLMap SBMLid="as5" COPASIkey="Metabolite_3"/>
    <SBMLMap SBMLid="as6" COPASIkey="Metabolite_4"/>
    <SBMLMap SBMLid="as7" COPASIkey="Metabolite_5"/>
    <SBMLMap SBMLid="as9" COPASIkey="Metabolite_6"/>
    <SBMLMap SBMLid="g1" COPASIkey="Metabolite_7"/>
    <SBMLMap SBMLid="g2" COPASIkey="Metabolite_8"/>
    <SBMLMap SBMLid="g3" COPASIkey="Metabolite_9"/>
    <SBMLMap SBMLid="g4" COPASIkey="Metabolite_10"/>
    <SBMLMap SBMLid="g5" COPASIkey="Metabolite_11"/>
    <SBMLMap SBMLid="g6" COPASIkey="Metabolite_12"/>
    <SBMLMap SBMLid="g7" COPASIkey="Metabolite_13"/>
    <SBMLMap SBMLid="g8" COPASIkey="Metabolite_14"/>
    <SBMLMap SBMLid="g9" COPASIkey="Metabolite_15"/>
    <SBMLMap SBMLid="p1" COPASIkey="Metabolite_16"/>
    <SBMLMap SBMLid="p1_degradation_rate" COPASIkey="ModelValue_2"/>
    <SBMLMap SBMLid="p2" COPASIkey="Metabolite_17"/>
    <SBMLMap SBMLid="p2_degradation_rate" COPASIkey="ModelValue_3"/>
    <SBMLMap SBMLid="p3" COPASIkey="Metabolite_18"/>
    <SBMLMap SBMLid="p3_degradation_rate" COPASIkey="ModelValue_4"/>
    <SBMLMap SBMLid="p4" COPASIkey="Metabolite_19"/>
    <SBMLMap SBMLid="p4_degradation_rate" COPASIkey="ModelValue_5"/>
    <SBMLMap SBMLid="p5" COPASIkey="Metabolite_20"/>
    <SBMLMap SBMLid="p5_degradation_rate" COPASIkey="ModelValue_6"/>
    <SBMLMap SBMLid="p6" COPASIkey="Metabolite_21"/>
    <SBMLMap SBMLid="p6_degradation_rate" COPASIkey="ModelValue_7"/>
    <SBMLMap SBMLid="p7" COPASIkey="Metabolite_22"/>
    <SBMLMap SBMLid="p7_degradation_rate" COPASIkey="ModelValue_8"/>
    <SBMLMap SBMLid="p8" COPASIkey="Metabolite_23"/>
    <SBMLMap SBMLid="p8_degradation_rate" COPASIkey="ModelValue_9"/>
    <SBMLMap SBMLid="p9" COPASIkey="Metabolite_24"/>
    <SBMLMap SBMLid="p9_degradation_rate" COPASIkey="ModelValue_10"/>
    <SBMLMap SBMLid="pro1" COPASIkey="Metabolite_25"/>
    <SBMLMap SBMLid="pro1_strength" COPASIkey="ModelValue_31"/>
    <SBMLMap SBMLid="pro2" COPASIkey="Metabolite_26"/>
    <SBMLMap SBMLid="pro2_strength" COPASIkey="ModelValue_32"/>
    <SBMLMap SBMLid="pro3" COPASIkey="Metabolite_27"/>
    <SBMLMap SBMLid="pro3_strength" COPASIkey="ModelValue_33"/>
    <SBMLMap SBMLid="pro4" COPASIkey="Metabolite_28"/>
    <SBMLMap SBMLid="pro4_strength" COPASIkey="ModelValue_34"/>
    <SBMLMap SBMLid="pro5" COPASIkey="Metabolite_29"/>
    <SBMLMap SBMLid="pro5_strength" COPASIkey="ModelValue_35"/>
    <SBMLMap SBMLid="pro6" COPASIkey="Metabolite_30"/>
    <SBMLMap SBMLid="pro6_strength" COPASIkey="ModelValue_37"/>
    <SBMLMap SBMLid="pro7" COPASIkey="Metabolite_31"/>
    <SBMLMap SBMLid="pro7_strength" COPASIkey="ModelValue_38"/>
    <SBMLMap SBMLid="pro8" COPASIkey="Metabolite_32"/>
    <SBMLMap SBMLid="pro8_strength" COPASIkey="ModelValue_39"/>
    <SBMLMap SBMLid="pro9" COPASIkey="Metabolite_33"/>
    <SBMLMap SBMLid="pro9_strength" COPASIkey="ModelValue_40"/>
    <SBMLMap SBMLid="r10_Kd" COPASIkey="ModelValue_42"/>
    <SBMLMap SBMLid="r10_h" COPASIkey="ModelValue_43"/>
    <SBMLMap SBMLid="r11_Kd" COPASIkey="ModelValue_44"/>
    <SBMLMap SBMLid="r11_h" COPASIkey="ModelValue_45"/>
    <SBMLMap SBMLid="r12_Kd" COPASIkey="ModelValue_46"/>
    <SBMLMap SBMLid="r12_h" COPASIkey="ModelValue_47"/>
    <SBMLMap SBMLid="r13_Kd" COPASIkey="ModelValue_48"/>
    <SBMLMap SBMLid="r13_h" COPASIkey="ModelValue_49"/>
    <SBMLMap SBMLid="r1_Kd" COPASIkey="ModelValue_11"/>
    <SBMLMap SBMLid="r1_h" COPASIkey="ModelValue_12"/>
    <SBMLMap SBMLid="r2_Kd" COPASIkey="ModelValue_13"/>
    <SBMLMap SBMLid="r2_h" COPASIkey="ModelValue_14"/>
    <SBMLMap SBMLid="r3_Kd" COPASIkey="ModelValue_15"/>
    <SBMLMap SBMLid="r3_h" COPASIkey="ModelValue_16"/>
    <SBMLMap SBMLid="r4_Kd" COPASIkey="ModelValue_17"/>
    <SBMLMap SBMLid="r4_h" COPASIkey="ModelValue_18"/>
    <SBMLMap SBMLid="r5_Kd" COPASIkey="ModelValue_19"/>
    <SBMLMap SBMLid="r5_h" COPASIkey="ModelValue_20"/>
    <SBMLMap SBMLid="r6_Kd" COPASIkey="ModelValue_21"/>
    <SBMLMap SBMLid="r6_h" COPASIkey="ModelValue_22"/>
    <SBMLMap SBMLid="r7_Kd" COPASIkey="ModelValue_23"/>
    <SBMLMap SBMLid="r7_h" COPASIkey="ModelValue_24"/>
    <SBMLMap SBMLid="r8_Kd" COPASIkey="ModelValue_25"/>
    <SBMLMap SBMLid="r8_h" COPASIkey="ModelValue_26"/>
    <SBMLMap SBMLid="r9_Kd" COPASIkey="ModelValue_27"/>
    <SBMLMap SBMLid="r9_h" COPASIkey="ModelValue_28"/>
    <SBMLMap SBMLid="rbs1" COPASIkey="Metabolite_34"/>
    <SBMLMap SBMLid="rbs1_strength" COPASIkey="ModelValue_51"/>
    <SBMLMap SBMLid="rbs2" COPASIkey="Metabolite_35"/>
    <SBMLMap SBMLid="rbs2_strength" COPASIkey="ModelValue_52"/>
    <SBMLMap SBMLid="rbs3" COPASIkey="Metabolite_36"/>
    <SBMLMap SBMLid="rbs3_strength" COPASIkey="ModelValue_53"/>
    <SBMLMap SBMLid="rbs4" COPASIkey="Metabolite_37"/>
    <SBMLMap SBMLid="rbs4_strength" COPASIkey="ModelValue_54"/>
    <SBMLMap SBMLid="rbs5" COPASIkey="Metabolite_38"/>
    <SBMLMap SBMLid="rbs5_strength" COPASIkey="ModelValue_55"/>
    <SBMLMap SBMLid="rbs6" COPASIkey="Metabolite_39"/>
    <SBMLMap SBMLid="rbs6_strength" COPASIkey="ModelValue_57"/>
    <SBMLMap SBMLid="rbs7" COPASIkey="Metabolite_40"/>
    <SBMLMap SBMLid="rbs7_strength" COPASIkey="ModelValue_58"/>
    <SBMLMap SBMLid="rbs8" COPASIkey="Metabolite_41"/>
    <SBMLMap SBMLid="rbs8_strength" COPASIkey="ModelValue_59"/>
    <SBMLMap SBMLid="rbs9" COPASIkey="Metabolite_42"/>
    <SBMLMap SBMLid="rbs9_strength" COPASIkey="ModelValue_60"/>
    <SBMLMap SBMLid="rs1a" COPASIkey="Metabolite_43"/>
    <SBMLMap SBMLid="rs1b" COPASIkey="Metabolite_44"/>
    <SBMLMap SBMLid="rs2" COPASIkey="Metabolite_45"/>
    <SBMLMap SBMLid="rs3" COPASIkey="Metabolite_46"/>
    <SBMLMap SBMLid="rs7" COPASIkey="Metabolite_47"/>
    <SBMLMap SBMLid="rs8" COPASIkey="Metabolite_48"/>
    <SBMLMap SBMLid="v1_mrna" COPASIkey="Metabolite_49"/>
    <SBMLMap SBMLid="v1_mrna_degradation_rate" COPASIkey="ModelValue_29"/>
    <SBMLMap SBMLid="v1_v1" COPASIkey="Reaction_32"/>
    <SBMLMap SBMLid="v1_v2" COPASIkey="Reaction_33"/>
    <SBMLMap SBMLid="v1_v3" COPASIkey="Reaction_34"/>
    <SBMLMap SBMLid="v1_v4" COPASIkey="Reaction_35"/>
    <SBMLMap SBMLid="v2_mrna" COPASIkey="Metabolite_50"/>
    <SBMLMap SBMLid="v2_mrna_degradation_rate" COPASIkey="ModelValue_30"/>
    <SBMLMap SBMLid="v2_v1" COPASIkey="Reaction_28"/>
    <SBMLMap SBMLid="v2_v2" COPASIkey="Reaction_29"/>
    <SBMLMap SBMLid="v2_v3" COPASIkey="Reaction_30"/>
    <SBMLMap SBMLid="v2_v4" COPASIkey="Reaction_31"/>
    <SBMLMap SBMLid="v3_mrna" COPASIkey="Metabolite_51"/>
    <SBMLMap SBMLid="v3_mrna_degradation_rate" COPASIkey="ModelValue_36"/>
    <SBMLMap SBMLid="v3_v1" COPASIkey="Reaction_24"/>
    <SBMLMap SBMLid="v3_v2" COPASIkey="Reaction_25"/>
    <SBMLMap SBMLid="v3_v3" COPASIkey="Reaction_26"/>
    <SBMLMap SBMLid="v3_v4" COPASIkey="Reaction_27"/>
    <SBMLMap SBMLid="v4_mrna" COPASIkey="Metabolite_52"/>
    <SBMLMap SBMLid="v4_mrna_degradation_rate" COPASIkey="ModelValue_41"/>
    <SBMLMap SBMLid="v4_v1" COPASIkey="Reaction_20"/>
    <SBMLMap SBMLid="v4_v2" COPASIkey="Reaction_21"/>
    <SBMLMap SBMLid="v4_v3" COPASIkey="Reaction_22"/>
    <SBMLMap SBMLid="v4_v4" COPASIkey="Reaction_23"/>
    <SBMLMap SBMLid="v5_mrna" COPASIkey="Metabolite_53"/>
    <SBMLMap SBMLid="v5_mrna_degradation_rate" COPASIkey="ModelValue_50"/>
    <SBMLMap SBMLid="v5_v1" COPASIkey="Reaction_16"/>
    <SBMLMap SBMLid="v5_v2" COPASIkey="Reaction_17"/>
    <SBMLMap SBMLid="v5_v3" COPASIkey="Reaction_18"/>
    <SBMLMap SBMLid="v5_v4" COPASIkey="Reaction_19"/>
    <SBMLMap SBMLid="v6_mrna" COPASIkey="Metabolite_54"/>
    <SBMLMap SBMLid="v6_mrna_degradation_rate" COPASIkey="ModelValue_56"/>
    <SBMLMap SBMLid="v6_v1" COPASIkey="Reaction_12"/>
    <SBMLMap SBMLid="v6_v2" COPASIkey="Reaction_13"/>
    <SBMLMap SBMLid="v6_v3" COPASIkey="Reaction_14"/>
    <SBMLMap SBMLid="v6_v4" COPASIkey="Reaction_15"/>
    <SBMLMap SBMLid="v7_mrna" COPASIkey="Metabolite_55"/>
    <SBMLMap SBMLid="v7_mrna_degradation_rate" COPASIkey="ModelValue_61"/>
    <SBMLMap SBMLid="v7_v1" COPASIkey="Reaction_8"/>
    <SBMLMap SBMLid="v7_v2" COPASIkey="Reaction_9"/>
    <SBMLMap SBMLid="v7_v3" COPASIkey="Reaction_10"/>
    <SBMLMap SBMLid="v7_v4" COPASIkey="Reaction_11"/>
    <SBMLMap SBMLid="v8_mrna" COPASIkey="Metabolite_56"/>
    <SBMLMap SBMLid="v8_mrna_degradation_rate" COPASIkey="ModelValue_0"/>
    <SBMLMap SBMLid="v8_v1" COPASIkey="Reaction_4"/>
    <SBMLMap SBMLid="v8_v2" COPASIkey="Reaction_5"/>
    <SBMLMap SBMLid="v8_v3" COPASIkey="Reaction_6"/>
    <SBMLMap SBMLid="v8_v4" COPASIkey="Reaction_7"/>
    <SBMLMap SBMLid="v9_mrna" COPASIkey="Metabolite_57"/>
    <SBMLMap SBMLid="v9_mrna_degradation_rate" COPASIkey="ModelValue_1"/>
    <SBMLMap SBMLid="v9_v1" COPASIkey="Reaction_0"/>
    <SBMLMap SBMLid="v9_v2" COPASIkey="Reaction_1"/>
    <SBMLMap SBMLid="v9_v3" COPASIkey="Reaction_2"/>
    <SBMLMap SBMLid="v9_v4" COPASIkey="Reaction_3"/>
  </SBMLReference>
</COPASI>
