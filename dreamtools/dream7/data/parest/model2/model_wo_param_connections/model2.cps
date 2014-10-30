<?xml version="1.0" encoding="UTF-8"?>
<!-- generated with COPASI 4.8 (Build 35) (http://www.copasi.org) at 2012-05-22 21:36:54 UTC -->
<?oxygen RNGSchema="http://www.copasi.org/static/schema/CopasiML.rng" type="xml"?>
<COPASI xmlns="http://www.copasi.org/static/schema" versionMajor="1" versionMinor="0" versionDevel="35">
  <ListOfFunctions>
    <Function key="Function_66" name="function_4__J0_2" type="UserDefined" reversible="false">
      <Expression>
        p1_synthesis_rate*(X/r1_Kd)^r1_h/(1+(X/r1_Kd)^r1_h)/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_500" name="X" order="0" role="substrate"/>
        <ParameterDescription key="FunctionParameter_499" name="compartment" order="1" role="volume"/>
        <ParameterDescription key="FunctionParameter_498" name="p1_synthesis_rate" order="2" role="constant"/>
        <ParameterDescription key="FunctionParameter_497" name="r1_Kd" order="3" role="constant"/>
        <ParameterDescription key="FunctionParameter_496" name="r1_h" order="4" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_91" name="function_4__J1_2" type="UserDefined" reversible="false">
      <Expression>
        p1_degradation_rate*p1/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_501" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_504" name="p1" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_490" name="p1_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_92" name="function_4__J2_2" type="UserDefined" reversible="unspecified">
      <Expression>
        p2_synthesis_rate*(p1/r2_Kd)^r2_h/(1+(p1/r2_Kd)^r2_h)/(1+(p6/r5_Kd)^r5_h)/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_481" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_480" name="p1" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_479" name="p2_synthesis_rate" order="2" role="constant"/>
        <ParameterDescription key="FunctionParameter_478" name="p6" order="3" role="modifier"/>
        <ParameterDescription key="FunctionParameter_477" name="r2_Kd" order="4" role="constant"/>
        <ParameterDescription key="FunctionParameter_476" name="r2_h" order="5" role="constant"/>
        <ParameterDescription key="FunctionParameter_475" name="r5_Kd" order="6" role="constant"/>
        <ParameterDescription key="FunctionParameter_474" name="r5_h" order="7" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_93" name="function_4__J3_2" type="UserDefined" reversible="false">
      <Expression>
        p2_degradation_rate*p2/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_505" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_485" name="p2" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_502" name="p2_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_94" name="function_4__J4_2" type="UserDefined" reversible="unspecified">
      <Expression>
        (p3_synthesis_rate_1*(p2/r4_Kd)^r4_h/(1+(p2/r4_Kd)^r4_h)+p3_synthesis_rate_2*(p1/r3_Kd)^r3_h/(1+(p1/r3_Kd)^r3_h))/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_458" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_457" name="p1" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_456" name="p2" order="2" role="modifier"/>
        <ParameterDescription key="FunctionParameter_455" name="p3_synthesis_rate_1" order="3" role="constant"/>
        <ParameterDescription key="FunctionParameter_454" name="p3_synthesis_rate_2" order="4" role="constant"/>
        <ParameterDescription key="FunctionParameter_453" name="r3_Kd" order="5" role="constant"/>
        <ParameterDescription key="FunctionParameter_452" name="r3_h" order="6" role="constant"/>
        <ParameterDescription key="FunctionParameter_451" name="r4_Kd" order="7" role="constant"/>
        <ParameterDescription key="FunctionParameter_450" name="r4_h" order="8" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_95" name="function_4__J5_2" type="UserDefined" reversible="false">
      <Expression>
        p3_degradation_rate*p3/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_461" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_463" name="p3" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_483" name="p3_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_96" name="function_4__J6_2" type="UserDefined" reversible="false">
      <Expression>
        p4_synthesis_rate_1*p3/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_440" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_439" name="p3" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_438" name="p4_synthesis_rate_1" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_97" name="function_4__J7_2" type="UserDefined" reversible="unspecified">
      <Expression>
        p4_synthesis_rate_2/(1+(p7/r8_Kd)^r8_h)/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_432" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_431" name="p4_synthesis_rate_2" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_430" name="p7" order="2" role="modifier"/>
        <ParameterDescription key="FunctionParameter_429" name="r8_Kd" order="3" role="constant"/>
        <ParameterDescription key="FunctionParameter_428" name="r8_h" order="4" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_98" name="function_4__J8_2" type="UserDefined" reversible="false">
      <Expression>
        p4_degradation_rate*p4/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_464" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_433" name="p4" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_422" name="p4_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_99" name="function_4__J9_2" type="UserDefined" reversible="unspecified">
      <Expression>
        (r6_basal+p5_synthesis_rate_1*(p4/r6_Kd)^r6_h/(1+(p4/r6_Kd)^r6_h)+p5_synthesis_rate_3*(p5/r7_Kd)^r7_h/(1+(p5/r7_Kd)^r7_h)+p5_synthesis_rate_2)/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_410" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_409" name="p4" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_408" name="p5" order="2" role="product"/>
        <ParameterDescription key="FunctionParameter_407" name="p5_synthesis_rate_1" order="3" role="constant"/>
        <ParameterDescription key="FunctionParameter_406" name="p5_synthesis_rate_2" order="4" role="constant"/>
        <ParameterDescription key="FunctionParameter_405" name="p5_synthesis_rate_3" order="5" role="constant"/>
        <ParameterDescription key="FunctionParameter_404" name="r6_Kd" order="6" role="constant"/>
        <ParameterDescription key="FunctionParameter_403" name="r6_basal" order="7" role="constant"/>
        <ParameterDescription key="FunctionParameter_402" name="r6_h" order="8" role="constant"/>
        <ParameterDescription key="FunctionParameter_401" name="r7_Kd" order="9" role="constant"/>
        <ParameterDescription key="FunctionParameter_400" name="r7_h" order="10" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_100" name="function_4__J10_2" type="UserDefined" reversible="false">
      <Expression>
        p5_degradation_rate*p5/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_434" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_418" name="p5" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_416" name="p5_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_101" name="function_4__J11_2" type="UserDefined" reversible="unspecified">
      <Expression>
        p6_synthesis_rate/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_417" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_486" name="p6_synthesis_rate" order="1" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_102" name="function_4__J12_2" type="UserDefined" reversible="false">
      <Expression>
        p6_degradation_rate*p6/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_375" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_385" name="p6" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_381" name="p6_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_103" name="function_4__J13_2" type="UserDefined" reversible="unspecified">
      <Expression>
        (r11_basal+p11_synthesis_rate_1*(p5/r11_Kd)^r11_h/(1+(p5/r11_Kd)^r11_h))/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_757" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_758" name="p11_synthesis_rate_1" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_759" name="p5" order="2" role="modifier"/>
        <ParameterDescription key="FunctionParameter_760" name="r11_Kd" order="3" role="constant"/>
        <ParameterDescription key="FunctionParameter_761" name="r11_basal" order="4" role="constant"/>
        <ParameterDescription key="FunctionParameter_762" name="r11_h" order="5" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_104" name="function_4__J14_2" type="UserDefined" reversible="false">
      <Expression>
        p11_degradation_rate*p11/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_367" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_414" name="p11" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_756" name="p11_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_105" name="function_4__J15_2" type="UserDefined" reversible="unspecified">
      <Expression>
        p7_synthesis_rate*(r11_basal+p11_synthesis_rate_1*(p5/r11_Kd)^r11_h/(1+(p5/r11_Kd)^r11_h))/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_776" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_777" name="p11_synthesis_rate_1" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_778" name="p5" order="2" role="modifier"/>
        <ParameterDescription key="FunctionParameter_779" name="p7_synthesis_rate" order="3" role="constant"/>
        <ParameterDescription key="FunctionParameter_780" name="r11_Kd" order="4" role="constant"/>
        <ParameterDescription key="FunctionParameter_781" name="r11_basal" order="5" role="constant"/>
        <ParameterDescription key="FunctionParameter_782" name="r11_h" order="6" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_106" name="function_4__J16_2" type="UserDefined" reversible="false">
      <Expression>
        p7_degradation_rate*p7/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_755" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_772" name="p7" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_736" name="p7_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_107" name="function_4__J17_2" type="UserDefined" reversible="unspecified">
      <Expression>
        p8_synthesis_rate/(1+(p7/r14_Kd)^r14_h)/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_794" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_795" name="p7" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_796" name="p8_synthesis_rate" order="2" role="constant"/>
        <ParameterDescription key="FunctionParameter_797" name="r14_Kd" order="3" role="constant"/>
        <ParameterDescription key="FunctionParameter_798" name="r14_h" order="4" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_108" name="function_4__J18_2" type="UserDefined" reversible="false">
      <Expression>
        p8_degradation_rate*p8/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_413" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_793" name="p8" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_804" name="p8_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_109" name="function_4__J19_2" type="UserDefined" reversible="unspecified">
      <Expression>
        p9_synthesis_rate*(p8/r15_Kd)^r15_h/(1+(p8/r15_Kd)^r15_h)/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_810" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_811" name="p8" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_812" name="p9_synthesis_rate" order="2" role="constant"/>
        <ParameterDescription key="FunctionParameter_813" name="r15_Kd" order="3" role="constant"/>
        <ParameterDescription key="FunctionParameter_814" name="r15_h" order="4" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_110" name="function_4__J20_2" type="UserDefined" reversible="false">
      <Expression>
        p9_degradation_rate*p9/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_773" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_809" name="p9" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_820" name="p9_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_111" name="function_4__J21_2" type="UserDefined" reversible="unspecified">
      <Expression>
        p10_synthesis_rate/(1+(p9/r16_Kd)^r16_h)/(1+(p7/r13_Kd)^r13_h)/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_829" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_830" name="p10_synthesis_rate" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_831" name="p7" order="2" role="modifier"/>
        <ParameterDescription key="FunctionParameter_832" name="p9" order="3" role="modifier"/>
        <ParameterDescription key="FunctionParameter_833" name="r13_Kd" order="4" role="constant"/>
        <ParameterDescription key="FunctionParameter_834" name="r13_h" order="5" role="constant"/>
        <ParameterDescription key="FunctionParameter_835" name="r16_Kd" order="6" role="constant"/>
        <ParameterDescription key="FunctionParameter_836" name="r16_h" order="7" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_112" name="function_4__J22_2" type="UserDefined" reversible="false">
      <Expression>
        p10_degradation_rate*p10/compartment
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_826" name="compartment" order="0" role="volume"/>
        <ParameterDescription key="FunctionParameter_774" name="p10" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_825" name="p10_degradation_rate" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
  </ListOfFunctions>
  <Model key="Model_0" name="subchallenge2_missing_connections" simulationType="time" timeUnit="s" volumeUnit="l" areaUnit="m²" lengthUnit="m" quantityUnit="mol" type="deterministic" avogadroConstant="6.02214179e+023">
    <MiriamAnnotation>
<rdf:RDF
   xmlns:dcterms="http://purl.org/dc/terms/"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="#Model_0">
    <dcterms:created>
      <rdf:Description>
        <dcterms:W3CDTF>2012-05-22T14:36:47Z</dcterms:W3CDTF>
      </rdf:Description>
    </dcterms:created>
  </rdf:Description>
</rdf:RDF>

    </MiriamAnnotation>
    <ListOfCompartments>
      <Compartment key="Compartment_0" name="compartment" simulationType="fixed" dimensionality="3">
      </Compartment>
    </ListOfCompartments>
    <ListOfMetabolites>
      <Metabolite key="Metabolite_13" name="X" simulationType="fixed" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_12" name="__src__" simulationType="fixed" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_11" name="__waste__" simulationType="fixed" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_10" name="p1" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_9" name="p2" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_8" name="p3" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_7" name="p4" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_6" name="p5" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_5" name="p6" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_4" name="p11" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_3" name="p7" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_2" name="p8" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_1" name="p9" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
      <Metabolite key="Metabolite_0" name="p10" simulationType="reactions" compartment="Compartment_0">
      </Metabolite>
    </ListOfMetabolites>
    <ListOfModelValues>
      <ModelValue key="ModelValue_60" name="p1_synthesis_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_59" name="r1_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_58" name="r1_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_57" name="p1_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_56" name="p2_synthesis_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_55" name="r2_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_54" name="r2_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_53" name="r5_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_52" name="r5_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_51" name="p2_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_50" name="p3_synthesis_rate_1" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_49" name="r4_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_48" name="r4_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_47" name="p3_synthesis_rate_2" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_46" name="r3_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_45" name="r3_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_44" name="p3_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_43" name="p4_synthesis_rate_1" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_42" name="p4_synthesis_rate_2" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_41" name="r8_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_40" name="r8_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_39" name="p4_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_38" name="r6_basal" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_37" name="p5_synthesis_rate_1" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_36" name="r6_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_35" name="r6_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_34" name="p5_synthesis_rate_3" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_33" name="r7_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_32" name="r7_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_31" name="p5_synthesis_rate_2" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_30" name="p5_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_29" name="p6_synthesis_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_28" name="p6_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_27" name="r11_basal" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_26" name="p11_synthesis_rate_1" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_25" name="r11_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_24" name="r11_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_23" name="p11_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_22" name="p7_synthesis_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_21" name="p7_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_20" name="p8_synthesis_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_19" name="r14_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_18" name="r14_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_17" name="p8_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_16" name="p9_synthesis_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_15" name="r15_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_14" name="r15_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_13" name="p9_degradation_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_12" name="p10_synthesis_rate" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_11" name="r16_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_10" name="r16_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_9" name="r13_Kd" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_8" name="r13_h" simulationType="fixed">
      </ModelValue>
      <ModelValue key="ModelValue_7" name="p10_degradation_rate" simulationType="fixed">
      </ModelValue>
    </ListOfModelValues>
    <ListOfReactions>
      <Reaction key="Reaction_22" name="_J0" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_13" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_10" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_1489" name="p1_synthesis_rate" value="1"/>
          <Constant key="Parameter_1490" name="r1_Kd" value="1"/>
          <Constant key="Parameter_1491" name="r1_h" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_66">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_500">
              <SourceParameter reference="Metabolite_13"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_499">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_498">
              <SourceParameter reference="ModelValue_60"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_497">
              <SourceParameter reference="ModelValue_59"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_496">
              <SourceParameter reference="ModelValue_58"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_21" name="_J1" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_10" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_1494" name="p1_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_91">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_501">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_504">
              <SourceParameter reference="Metabolite_10"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_490">
              <SourceParameter reference="ModelValue_57"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_20" name="_J2" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_9" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_10" stoichiometry="2"/>
          <Modifier metabolite="Metabolite_5" stoichiometry="2"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1495" name="p2_synthesis_rate" value="1"/>
          <Constant key="Parameter_1496" name="r2_Kd" value="1"/>
          <Constant key="Parameter_1492" name="r2_h" value="1"/>
          <Constant key="Parameter_1493" name="r5_Kd" value="1"/>
          <Constant key="Parameter_1497" name="r5_h" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_92">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_481">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_480">
              <SourceParameter reference="Metabolite_10"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_479">
              <SourceParameter reference="ModelValue_56"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_478">
              <SourceParameter reference="Metabolite_5"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_477">
              <SourceParameter reference="ModelValue_55"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_476">
              <SourceParameter reference="ModelValue_54"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_475">
              <SourceParameter reference="ModelValue_53"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_474">
              <SourceParameter reference="ModelValue_52"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_19" name="_J3" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_9" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_1498" name="p2_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_93">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_505">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_485">
              <SourceParameter reference="Metabolite_9"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_502">
              <SourceParameter reference="ModelValue_51"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_18" name="_J4" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_8" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_9" stoichiometry="2"/>
          <Modifier metabolite="Metabolite_10" stoichiometry="2"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1499" name="p3_synthesis_rate_1" value="1"/>
          <Constant key="Parameter_1500" name="p3_synthesis_rate_2" value="1"/>
          <Constant key="Parameter_1501" name="r3_Kd" value="1"/>
          <Constant key="Parameter_1502" name="r3_h" value="1"/>
          <Constant key="Parameter_1503" name="r4_Kd" value="1"/>
          <Constant key="Parameter_1504" name="r4_h" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_94">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_458">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_457">
              <SourceParameter reference="Metabolite_10"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_456">
              <SourceParameter reference="Metabolite_9"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_455">
              <SourceParameter reference="ModelValue_50"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_454">
              <SourceParameter reference="ModelValue_47"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_453">
              <SourceParameter reference="ModelValue_46"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_452">
              <SourceParameter reference="ModelValue_45"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_451">
              <SourceParameter reference="ModelValue_49"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_450">
              <SourceParameter reference="ModelValue_48"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_17" name="_J5" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_8" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_1505" name="p3_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_95">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_461">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_463">
              <SourceParameter reference="Metabolite_8"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_483">
              <SourceParameter reference="ModelValue_44"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_16" name="_J6" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_8" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_7" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_1506" name="p4_synthesis_rate_1" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_96">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_440">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_439">
              <SourceParameter reference="Metabolite_8"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_438">
              <SourceParameter reference="ModelValue_43"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_15" name="_J7" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_7" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_3" stoichiometry="2"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1507" name="p4_synthesis_rate_2" value="1"/>
          <Constant key="Parameter_1508" name="r8_Kd" value="1"/>
          <Constant key="Parameter_1509" name="r8_h" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_97">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_432">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_431">
              <SourceParameter reference="ModelValue_42"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_430">
              <SourceParameter reference="Metabolite_3"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_429">
              <SourceParameter reference="ModelValue_41"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_428">
              <SourceParameter reference="ModelValue_40"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_14" name="_J8" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_7" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_1510" name="p4_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_98">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_464">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_433">
              <SourceParameter reference="Metabolite_7"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_422">
              <SourceParameter reference="ModelValue_39"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_13" name="_J9" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_6" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_7" stoichiometry="2"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1511" name="p5_synthesis_rate_1" value="1"/>
          <Constant key="Parameter_1512" name="p5_synthesis_rate_2" value="1"/>
          <Constant key="Parameter_1515" name="p5_synthesis_rate_3" value="1"/>
          <Constant key="Parameter_1514" name="r6_Kd" value="1"/>
          <Constant key="Parameter_1513" name="r6_basal" value="1"/>
          <Constant key="Parameter_1516" name="r6_h" value="1"/>
          <Constant key="Parameter_1517" name="r7_Kd" value="1"/>
          <Constant key="Parameter_1519" name="r7_h" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_99">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_410">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_409">
              <SourceParameter reference="Metabolite_7"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_408">
              <SourceParameter reference="Metabolite_6"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_407">
              <SourceParameter reference="ModelValue_37"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_406">
              <SourceParameter reference="ModelValue_31"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_405">
              <SourceParameter reference="ModelValue_34"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_404">
              <SourceParameter reference="ModelValue_36"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_403">
              <SourceParameter reference="ModelValue_38"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_402">
              <SourceParameter reference="ModelValue_35"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_401">
              <SourceParameter reference="ModelValue_33"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_400">
              <SourceParameter reference="ModelValue_32"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_12" name="_J10" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_6" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_1520" name="p5_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_100">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_434">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_418">
              <SourceParameter reference="Metabolite_6"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_416">
              <SourceParameter reference="ModelValue_30"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_11" name="_J11" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_5" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_1518" name="p6_synthesis_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_101">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_417">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_486">
              <SourceParameter reference="ModelValue_29"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_10" name="_J12" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_5" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_1521" name="p6_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_102">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_375">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_385">
              <SourceParameter reference="Metabolite_5"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_381">
              <SourceParameter reference="ModelValue_28"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_9" name="_J13" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_4" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_6" stoichiometry="2"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1522" name="p11_synthesis_rate_1" value="1"/>
          <Constant key="Parameter_1523" name="r11_Kd" value="1"/>
          <Constant key="Parameter_1524" name="r11_basal" value="1"/>
          <Constant key="Parameter_1525" name="r11_h" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_103">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_757">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_758">
              <SourceParameter reference="ModelValue_26"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_759">
              <SourceParameter reference="Metabolite_6"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_760">
              <SourceParameter reference="ModelValue_25"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_761">
              <SourceParameter reference="ModelValue_27"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_762">
              <SourceParameter reference="ModelValue_24"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_8" name="_J14" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_4" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_1526" name="p11_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_104">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_367">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_414">
              <SourceParameter reference="Metabolite_4"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_756">
              <SourceParameter reference="ModelValue_23"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_7" name="_J15" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_3" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_6" stoichiometry="2"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1527" name="p11_synthesis_rate_1" value="1"/>
          <Constant key="Parameter_1528" name="p7_synthesis_rate" value="1"/>
          <Constant key="Parameter_1529" name="r11_Kd" value="1"/>
          <Constant key="Parameter_1530" name="r11_basal" value="1"/>
          <Constant key="Parameter_1531" name="r11_h" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_105">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_776">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_777">
              <SourceParameter reference="ModelValue_26"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_778">
              <SourceParameter reference="Metabolite_6"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_779">
              <SourceParameter reference="ModelValue_22"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_780">
              <SourceParameter reference="ModelValue_25"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_781">
              <SourceParameter reference="ModelValue_27"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_782">
              <SourceParameter reference="ModelValue_24"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_6" name="_J16" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_3" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_1532" name="p7_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_106">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_755">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_772">
              <SourceParameter reference="Metabolite_3"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_736">
              <SourceParameter reference="ModelValue_21"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_5" name="_J17" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_2" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_3" stoichiometry="2"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1533" name="p8_synthesis_rate" value="1"/>
          <Constant key="Parameter_1534" name="r14_Kd" value="1"/>
          <Constant key="Parameter_1535" name="r14_h" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_107">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_794">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_795">
              <SourceParameter reference="Metabolite_3"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_796">
              <SourceParameter reference="ModelValue_20"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_797">
              <SourceParameter reference="ModelValue_19"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_798">
              <SourceParameter reference="ModelValue_18"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_4" name="_J18" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_2" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_1536" name="p8_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_108">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_413">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_793">
              <SourceParameter reference="Metabolite_2"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_804">
              <SourceParameter reference="ModelValue_17"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_3" name="_J19" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_2" stoichiometry="2"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1537" name="p9_synthesis_rate" value="1"/>
          <Constant key="Parameter_1538" name="r15_Kd" value="1"/>
          <Constant key="Parameter_1539" name="r15_h" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_109">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_810">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_811">
              <SourceParameter reference="Metabolite_2"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_812">
              <SourceParameter reference="ModelValue_16"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_813">
              <SourceParameter reference="ModelValue_15"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_814">
              <SourceParameter reference="ModelValue_14"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_2" name="_J20" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_1540" name="p9_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_110">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_773">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_809">
              <SourceParameter reference="Metabolite_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_820">
              <SourceParameter reference="ModelValue_13"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_1" name="_J21" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_0" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_1" stoichiometry="2"/>
          <Modifier metabolite="Metabolite_3" stoichiometry="2"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_1541" name="p10_synthesis_rate" value="1"/>
          <Constant key="Parameter_1542" name="r13_Kd" value="1"/>
          <Constant key="Parameter_1543" name="r13_h" value="1"/>
          <Constant key="Parameter_1544" name="r16_Kd" value="1"/>
          <Constant key="Parameter_1545" name="r16_h" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_111">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_829">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_830">
              <SourceParameter reference="ModelValue_12"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_831">
              <SourceParameter reference="Metabolite_3"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_832">
              <SourceParameter reference="Metabolite_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_833">
              <SourceParameter reference="ModelValue_9"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_834">
              <SourceParameter reference="ModelValue_8"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_835">
              <SourceParameter reference="ModelValue_11"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_836">
              <SourceParameter reference="ModelValue_10"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_0" name="_J22" reversible="false">
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_0" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_1546" name="p10_degradation_rate" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_112">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_826">
              <SourceParameter reference="Compartment_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_774">
              <SourceParameter reference="Metabolite_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_825">
              <SourceParameter reference="ModelValue_7"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
    </ListOfReactions>
    <StateTemplate>
      <StateTemplateVariable objectReference="Model_0"/>
      <StateTemplateVariable objectReference="Metabolite_8"/>
      <StateTemplateVariable objectReference="Metabolite_7"/>
      <StateTemplateVariable objectReference="Metabolite_10"/>
      <StateTemplateVariable objectReference="Metabolite_9"/>
      <StateTemplateVariable objectReference="Metabolite_6"/>
      <StateTemplateVariable objectReference="Metabolite_5"/>
      <StateTemplateVariable objectReference="Metabolite_4"/>
      <StateTemplateVariable objectReference="Metabolite_3"/>
      <StateTemplateVariable objectReference="Metabolite_2"/>
      <StateTemplateVariable objectReference="Metabolite_1"/>
      <StateTemplateVariable objectReference="Metabolite_0"/>
      <StateTemplateVariable objectReference="Metabolite_13"/>
      <StateTemplateVariable objectReference="Metabolite_12"/>
      <StateTemplateVariable objectReference="Metabolite_11"/>
      <StateTemplateVariable objectReference="ModelValue_60"/>
      <StateTemplateVariable objectReference="ModelValue_59"/>
      <StateTemplateVariable objectReference="ModelValue_58"/>
      <StateTemplateVariable objectReference="ModelValue_57"/>
      <StateTemplateVariable objectReference="ModelValue_56"/>
      <StateTemplateVariable objectReference="ModelValue_55"/>
      <StateTemplateVariable objectReference="ModelValue_54"/>
      <StateTemplateVariable objectReference="ModelValue_53"/>
      <StateTemplateVariable objectReference="ModelValue_52"/>
      <StateTemplateVariable objectReference="ModelValue_51"/>
      <StateTemplateVariable objectReference="ModelValue_50"/>
      <StateTemplateVariable objectReference="ModelValue_49"/>
      <StateTemplateVariable objectReference="ModelValue_48"/>
      <StateTemplateVariable objectReference="ModelValue_47"/>
      <StateTemplateVariable objectReference="ModelValue_46"/>
      <StateTemplateVariable objectReference="ModelValue_45"/>
      <StateTemplateVariable objectReference="ModelValue_44"/>
      <StateTemplateVariable objectReference="ModelValue_43"/>
      <StateTemplateVariable objectReference="ModelValue_42"/>
      <StateTemplateVariable objectReference="ModelValue_41"/>
      <StateTemplateVariable objectReference="ModelValue_40"/>
      <StateTemplateVariable objectReference="ModelValue_39"/>
      <StateTemplateVariable objectReference="ModelValue_38"/>
      <StateTemplateVariable objectReference="ModelValue_37"/>
      <StateTemplateVariable objectReference="ModelValue_36"/>
      <StateTemplateVariable objectReference="ModelValue_35"/>
      <StateTemplateVariable objectReference="ModelValue_34"/>
      <StateTemplateVariable objectReference="ModelValue_33"/>
      <StateTemplateVariable objectReference="ModelValue_32"/>
      <StateTemplateVariable objectReference="ModelValue_31"/>
      <StateTemplateVariable objectReference="ModelValue_30"/>
      <StateTemplateVariable objectReference="ModelValue_29"/>
      <StateTemplateVariable objectReference="ModelValue_28"/>
      <StateTemplateVariable objectReference="ModelValue_27"/>
      <StateTemplateVariable objectReference="ModelValue_26"/>
      <StateTemplateVariable objectReference="ModelValue_25"/>
      <StateTemplateVariable objectReference="ModelValue_24"/>
      <StateTemplateVariable objectReference="ModelValue_23"/>
      <StateTemplateVariable objectReference="ModelValue_22"/>
      <StateTemplateVariable objectReference="ModelValue_21"/>
      <StateTemplateVariable objectReference="ModelValue_20"/>
      <StateTemplateVariable objectReference="ModelValue_19"/>
      <StateTemplateVariable objectReference="ModelValue_18"/>
      <StateTemplateVariable objectReference="ModelValue_17"/>
      <StateTemplateVariable objectReference="ModelValue_16"/>
      <StateTemplateVariable objectReference="ModelValue_15"/>
      <StateTemplateVariable objectReference="ModelValue_14"/>
      <StateTemplateVariable objectReference="ModelValue_13"/>
      <StateTemplateVariable objectReference="ModelValue_12"/>
      <StateTemplateVariable objectReference="ModelValue_11"/>
      <StateTemplateVariable objectReference="ModelValue_10"/>
      <StateTemplateVariable objectReference="ModelValue_9"/>
      <StateTemplateVariable objectReference="ModelValue_8"/>
      <StateTemplateVariable objectReference="ModelValue_7"/>
      <StateTemplateVariable objectReference="Compartment_0"/>
    </StateTemplate>
    <InitialState type="initialState">
      0 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 6.02214179e+023 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    </InitialState>
  </Model>
  <ListOfTasks>
    <Task key="Task_11" name="Steady-State" type="steadyState" scheduled="false" updateModel="false">
      <Report reference="Report_0" target="" append="1"/>
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
    <Task key="Task_1" name="Time-Course" type="timeCourse" scheduled="false" updateModel="false">
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
    <Task key="Task_2" name="Scan" type="scan" scheduled="false" updateModel="false">
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
    <Task key="Task_3" name="Elementary Flux Modes" type="fluxMode" scheduled="false" updateModel="false">
      <Report reference="Report_1" target="" append="1"/>
      <Problem>
      </Problem>
      <Method name="EFM Algorithm" type="EFMAlgorithm">
      </Method>
    </Task>
    <Task key="Task_4" name="Optimization" type="optimization" scheduled="false" updateModel="false">
      <Report reference="Report_2" target="" append="1"/>
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
      <Report reference="Report_3" target="" append="1"/>
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
    <Task key="Task_6" name="Metabolic Control Analysis" type="metabolicControlAnalysis" scheduled="false" updateModel="false">
      <Report reference="Report_4" target="" append="1"/>
      <Problem>
        <Parameter name="Steady-State" type="key" value="Task_11"/>
      </Problem>
      <Method name="MCA Method (Reder)" type="MCAMethod(Reder)">
        <Parameter name="Modulation Factor" type="unsignedFloat" value="1e-009"/>
      </Method>
    </Task>
    <Task key="Task_7" name="Lyapunov Exponents" type="lyapunovExponents" scheduled="false" updateModel="false">
      <Report reference="Report_5" target="" append="1"/>
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
    <Task key="Task_8" name="Time Scale Separation Analysis" type="timeScaleSeparationAnalysis" scheduled="false" updateModel="false">
      <Report reference="Report_6" target="" append="1"/>
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
    <Task key="Task_9" name="Sensitivities" type="sensitivities" scheduled="false" updateModel="false">
      <Report reference="Report_7" target="" append="1"/>
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
    <Task key="Task_33" name="Moieties" type="moieties" scheduled="false" updateModel="false">
      <Problem>
      </Problem>
      <Method name="Householder Reduction" type="Householder">
      </Method>
    </Task>
  </ListOfTasks>
  <ListOfReports>
    <Report key="Report_0" name="Steady-State" taskType="steadyState" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Footer>
        <Object cn="CN=Root,Vector=TaskList[Steady-State]"/>
      </Footer>
    </Report>
    <Report key="Report_1" name="Elementary Flux Modes" taskType="fluxMode" separator="&#x09;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Footer>
        <Object cn="CN=Root,Vector=TaskList[Elementary Flux Modes],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_2" name="Optimization" taskType="optimization" separator="&#x09;" precision="6">
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
    <Report key="Report_3" name="Parameter Estimation" taskType="parameterFitting" separator="&#x09;" precision="6">
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
    <Report key="Report_4" name="Metabolic Control Analysis" taskType="metabolicControlAnalysis" separator="&#x09;" precision="6">
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
    <Report key="Report_5" name="Lyapunov Exponents" taskType="lyapunovExponents" separator="&#x09;" precision="6">
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
    <Report key="Report_6" name="Time Scale Separation Analysis" taskType="timeScaleSeparationAnalysis" separator="&#x09;" precision="6">
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
    <Report key="Report_7" name="Sensitivities" taskType="sensitivities" separator="&#x09;" precision="6">
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
  <SBMLReference file="subchallenge2_missing_connections.xml">
    <SBMLMap SBMLid="X" COPASIkey="Metabolite_13"/>
    <SBMLMap SBMLid="_J0" COPASIkey="Reaction_22"/>
    <SBMLMap SBMLid="_J1" COPASIkey="Reaction_21"/>
    <SBMLMap SBMLid="_J10" COPASIkey="Reaction_12"/>
    <SBMLMap SBMLid="_J11" COPASIkey="Reaction_11"/>
    <SBMLMap SBMLid="_J12" COPASIkey="Reaction_10"/>
    <SBMLMap SBMLid="_J13" COPASIkey="Reaction_9"/>
    <SBMLMap SBMLid="_J14" COPASIkey="Reaction_8"/>
    <SBMLMap SBMLid="_J15" COPASIkey="Reaction_7"/>
    <SBMLMap SBMLid="_J16" COPASIkey="Reaction_6"/>
    <SBMLMap SBMLid="_J17" COPASIkey="Reaction_5"/>
    <SBMLMap SBMLid="_J18" COPASIkey="Reaction_4"/>
    <SBMLMap SBMLid="_J19" COPASIkey="Reaction_3"/>
    <SBMLMap SBMLid="_J2" COPASIkey="Reaction_20"/>
    <SBMLMap SBMLid="_J20" COPASIkey="Reaction_2"/>
    <SBMLMap SBMLid="_J21" COPASIkey="Reaction_1"/>
    <SBMLMap SBMLid="_J22" COPASIkey="Reaction_0"/>
    <SBMLMap SBMLid="_J3" COPASIkey="Reaction_19"/>
    <SBMLMap SBMLid="_J4" COPASIkey="Reaction_18"/>
    <SBMLMap SBMLid="_J5" COPASIkey="Reaction_17"/>
    <SBMLMap SBMLid="_J6" COPASIkey="Reaction_16"/>
    <SBMLMap SBMLid="_J7" COPASIkey="Reaction_15"/>
    <SBMLMap SBMLid="_J8" COPASIkey="Reaction_14"/>
    <SBMLMap SBMLid="_J9" COPASIkey="Reaction_13"/>
    <SBMLMap SBMLid="__src__" COPASIkey="Metabolite_12"/>
    <SBMLMap SBMLid="__waste__" COPASIkey="Metabolite_11"/>
    <SBMLMap SBMLid="compartment" COPASIkey="Compartment_0"/>
    <SBMLMap SBMLid="p1" COPASIkey="Metabolite_10"/>
    <SBMLMap SBMLid="p10" COPASIkey="Metabolite_0"/>
    <SBMLMap SBMLid="p10_degradation_rate" COPASIkey="ModelValue_7"/>
    <SBMLMap SBMLid="p10_synthesis_rate" COPASIkey="ModelValue_12"/>
    <SBMLMap SBMLid="p11" COPASIkey="Metabolite_4"/>
    <SBMLMap SBMLid="p11_degradation_rate" COPASIkey="ModelValue_23"/>
    <SBMLMap SBMLid="p11_synthesis_rate_1" COPASIkey="ModelValue_26"/>
    <SBMLMap SBMLid="p1_degradation_rate" COPASIkey="ModelValue_57"/>
    <SBMLMap SBMLid="p1_synthesis_rate" COPASIkey="ModelValue_60"/>
    <SBMLMap SBMLid="p2" COPASIkey="Metabolite_9"/>
    <SBMLMap SBMLid="p2_degradation_rate" COPASIkey="ModelValue_51"/>
    <SBMLMap SBMLid="p2_synthesis_rate" COPASIkey="ModelValue_56"/>
    <SBMLMap SBMLid="p3" COPASIkey="Metabolite_8"/>
    <SBMLMap SBMLid="p3_degradation_rate" COPASIkey="ModelValue_44"/>
    <SBMLMap SBMLid="p3_synthesis_rate_1" COPASIkey="ModelValue_50"/>
    <SBMLMap SBMLid="p3_synthesis_rate_2" COPASIkey="ModelValue_47"/>
    <SBMLMap SBMLid="p4" COPASIkey="Metabolite_7"/>
    <SBMLMap SBMLid="p4_degradation_rate" COPASIkey="ModelValue_39"/>
    <SBMLMap SBMLid="p4_synthesis_rate_1" COPASIkey="ModelValue_43"/>
    <SBMLMap SBMLid="p4_synthesis_rate_2" COPASIkey="ModelValue_42"/>
    <SBMLMap SBMLid="p5" COPASIkey="Metabolite_6"/>
    <SBMLMap SBMLid="p5_degradation_rate" COPASIkey="ModelValue_30"/>
    <SBMLMap SBMLid="p5_synthesis_rate_1" COPASIkey="ModelValue_37"/>
    <SBMLMap SBMLid="p5_synthesis_rate_2" COPASIkey="ModelValue_31"/>
    <SBMLMap SBMLid="p5_synthesis_rate_3" COPASIkey="ModelValue_34"/>
    <SBMLMap SBMLid="p6" COPASIkey="Metabolite_5"/>
    <SBMLMap SBMLid="p6_degradation_rate" COPASIkey="ModelValue_28"/>
    <SBMLMap SBMLid="p6_synthesis_rate" COPASIkey="ModelValue_29"/>
    <SBMLMap SBMLid="p7" COPASIkey="Metabolite_3"/>
    <SBMLMap SBMLid="p7_degradation_rate" COPASIkey="ModelValue_21"/>
    <SBMLMap SBMLid="p7_synthesis_rate" COPASIkey="ModelValue_22"/>
    <SBMLMap SBMLid="p8" COPASIkey="Metabolite_2"/>
    <SBMLMap SBMLid="p8_degradation_rate" COPASIkey="ModelValue_17"/>
    <SBMLMap SBMLid="p8_synthesis_rate" COPASIkey="ModelValue_20"/>
    <SBMLMap SBMLid="p9" COPASIkey="Metabolite_1"/>
    <SBMLMap SBMLid="p9_degradation_rate" COPASIkey="ModelValue_13"/>
    <SBMLMap SBMLid="p9_synthesis_rate" COPASIkey="ModelValue_16"/>
    <SBMLMap SBMLid="r11_Kd" COPASIkey="ModelValue_25"/>
    <SBMLMap SBMLid="r11_basal" COPASIkey="ModelValue_27"/>
    <SBMLMap SBMLid="r11_h" COPASIkey="ModelValue_24"/>
    <SBMLMap SBMLid="r13_Kd" COPASIkey="ModelValue_9"/>
    <SBMLMap SBMLid="r13_h" COPASIkey="ModelValue_8"/>
    <SBMLMap SBMLid="r14_Kd" COPASIkey="ModelValue_19"/>
    <SBMLMap SBMLid="r14_h" COPASIkey="ModelValue_18"/>
    <SBMLMap SBMLid="r15_Kd" COPASIkey="ModelValue_15"/>
    <SBMLMap SBMLid="r15_h" COPASIkey="ModelValue_14"/>
    <SBMLMap SBMLid="r16_Kd" COPASIkey="ModelValue_11"/>
    <SBMLMap SBMLid="r16_h" COPASIkey="ModelValue_10"/>
    <SBMLMap SBMLid="r1_Kd" COPASIkey="ModelValue_59"/>
    <SBMLMap SBMLid="r1_h" COPASIkey="ModelValue_58"/>
    <SBMLMap SBMLid="r2_Kd" COPASIkey="ModelValue_55"/>
    <SBMLMap SBMLid="r2_h" COPASIkey="ModelValue_54"/>
    <SBMLMap SBMLid="r3_Kd" COPASIkey="ModelValue_46"/>
    <SBMLMap SBMLid="r3_h" COPASIkey="ModelValue_45"/>
    <SBMLMap SBMLid="r4_Kd" COPASIkey="ModelValue_49"/>
    <SBMLMap SBMLid="r4_h" COPASIkey="ModelValue_48"/>
    <SBMLMap SBMLid="r5_Kd" COPASIkey="ModelValue_53"/>
    <SBMLMap SBMLid="r5_h" COPASIkey="ModelValue_52"/>
    <SBMLMap SBMLid="r6_Kd" COPASIkey="ModelValue_36"/>
    <SBMLMap SBMLid="r6_basal" COPASIkey="ModelValue_38"/>
    <SBMLMap SBMLid="r6_h" COPASIkey="ModelValue_35"/>
    <SBMLMap SBMLid="r7_Kd" COPASIkey="ModelValue_33"/>
    <SBMLMap SBMLid="r7_h" COPASIkey="ModelValue_32"/>
    <SBMLMap SBMLid="r8_Kd" COPASIkey="ModelValue_41"/>
    <SBMLMap SBMLid="r8_h" COPASIkey="ModelValue_40"/>
  </SBMLReference>
</COPASI>
