import groovy.json.*
import com.eviware.soapui.support.types.StringToStringMap 
import com.eviware.soapui.SoapUI
import com.eviware.soapui.settings.HttpSettings
import java.security.*
import javax.crypto.*
import javax.crypto.spec.*
import java.security.InvalidKeyException;
import static java.nio.charset.StandardCharsets.UTF_8
import com.eviware.soapui.support.types.StringToStringMap 
import java.security.MessageDigest
import groovy.time.TimeCategory
import java.util.Base64
import javax.crypto.Cipher
import java.nio.file.*
import java.security.spec.PKCS8EncodedKeySpec
// Send received request to https://example.org/soap/service
//def queryString = mockRequest.getPath() 
//def soapRequest = mockRequest.requestContent
//def soapRequestPath = mockRequest.requestHeaders
if(context.trx == "transfer"){

def today = new Date()
def date0 = today.format("yyyy-MM-dd")
def jam = today.format("HH:mm:ss")
def todaydate = new Date()
def tomorrowdate = todaydate.next()
def vyesterday = todaydate.previous()

use( TimeCategory ) {
    gmtdate = todaydate - 7.hours
}
gmtdate.format("yyyy-MM-dd'T'HH:mm:ss'Z'")
headBICSender = context.headBICSender
headBICReceiver = context.headBICReceiver
headBizMsgIdr = context.headBizMsgIdr
headMsgDefIdr = context.headMsgDefIdr
headBizSvc = context.headBizSvc
headCreDt = gmtdate.format("yyyy-MM-dd'T'HH:mm:'00Z'")
DocMsgId = context.DocMsgId
DocCreDtTm = context.DocCreDtTm
DocOrgnlMsgId = context.DocOrgnlMsgId
DocOrgnlMsgNmId = context.DocOrgnlMsgNmId
DocOrgnlEndToEndId = context.DocOrgnlEndToEndId
DocOrgnlTxId = context.DocOrgnlTxId
DocTxSts = context.DocTxSts
DocRsnPrtry = context.DocRsnPrtry
DocAddtlInf = context.DocAddtlInf
DocOrgnlTxRefIntrBkSttlmDt = context.DocOrgnlTxRefIntrBkSttlmDt
DocOrgnlTxRefPtyNm = context.DocOrgnlTxRefPtyNm
DocCdtrTp = context.DocCdtrTp
DocCdtrId = context.DocCdtrId
DocRsdntSts = context.DocRsdntSts
DocCdtrTwnNm = context.DocCdtrTwnNm

ReqTrf = context.ReqTrf
def slurper = new JsonSlurper()
def JsonRQ = slurper.parseText(ReqTrf)
log.warn JsonRQ

def Reqmap = [:]
JsonRQ.each{
	Reqmap[it.key] = it.value
	}
def docDbtrNm = Reqmap.BusMsg.Document.FIToFICstmrCdtTrf.CdtTrfTxInf[0].Dbtr.Nm
def docDbtrAcctId = Reqmap.BusMsg.Document.FIToFICstmrCdtTrf.CdtTrfTxInf[0].DbtrAcct.Id.Othr.Id
def docDbtrAcctTp = Reqmap.BusMsg.Document.FIToFICstmrCdtTrf.CdtTrfTxInf[0].DbtrAcct.Tp.Prtry
def docCdtrAcctId = Reqmap.BusMsg.Document.FIToFICstmrCdtTrf.CdtTrfTxInf[0].CdtrAcct.Id.Othr.Id
def docCdtrAcctTp = Reqmap.BusMsg.Document.FIToFICstmrCdtTrf.CdtTrfTxInf[0].CdtrAcct.Tp.Prtry
def docCdtrAgt = Reqmap.BusMsg.Document.FIToFICstmrCdtTrf.CdtTrfTxInf[0].CdtrAgt.FinInstnId.Othr.Id
def docDbtrAgt = Reqmap.BusMsg.Document.FIToFICstmrCdtTrf.CdtTrfTxInf[0].DbtrAgt.FinInstnId.Othr.Id

 def  output = [
            BusMsg : [
                    AppHdr : [
                            Fr : [
                                    FIId : [
                                            FinInstnId : [
                                                    Othr : [
                                                            Id : headBICSender
                                                    ]
                                            ]
                                    ]
                            ],
                            To : [
                                    FIId : [
                                            FinInstnId : [
                                                    Othr : [
                                                            Id : headBICReceiver
                                                    ]
                                            ]
                                    ]
                            ],
                            BizMsgIdr : headBizMsgIdr,
                            MsgDefIdr : headMsgDefIdr,
                            CreDt : headCreDt,
                    ],
                    Document : [
                            FIToFIPmtStsRpt : [
                                    GrpHdr : [
                                            MsgId : DocMsgId,
                                            CreDtTm : DocCreDtTm,
                                    ],
                                    OrgnlGrpInfAndSts : [[
                                            OrgnlMsgId : DocOrgnlMsgId,
                                            OrgnlMsgNmId : DocOrgnlMsgNmId,
                                    ]],
                                    TxInfAndSts : [[
                                            OrgnlEndToEndId : DocOrgnlEndToEndId,
                                            OrgnlTxId : DocOrgnlTxId,
                                            TxSts : "ACSC",
                                            StsRsnInf : [[
                                                    Rsn :[
                                                            Prtry : "U000"
                                                    ],
                                                    //AddtlInf : DocAddtlInf, //Add
                                            ]],
                                            OrgnlTxRef : [
                                                    IntrBkSttlmDt : DocOrgnlTxRefIntrBkSttlmDt,
                                                    Cdtr : [
                                                            Pty :[
                                                                    Nm : DocOrgnlTxRefPtyNm
                                                            ]
                                                    ],
                                                    DbtrAcct : [
                                                            Id :[
                                                                    Othr : [
                                                                    	Id : docDbtrAcctId
                                                                    ]
                                                            ],
                                                            Tp : [
                                                            	Prty : docDbtrAcctTp
                                                            ]
                                                    ],
                                                    Dbtr : [
                                                            Pty :[
                                                                    Nm : docDbtrNm
                                                            ]
                                                    ],
                                                    CdtrAcct : [
                                                            Id :[
                                                                    Othr : [
                                                                    	Id : docCdtrAcctId
                                                                    ]
                                                            ],
                                                            Tp : [
                                                            	Prty : docCdtrAcctTp
                                                            ]
                                                    ],
                                                    DbtrAgt : [
                                                            FinInstnId :[
                                                                    Othr : [
                                                                    	Id : docDbtrAgt
                                                                    ]
                                                            ]
                                                    ],
                                                    CdtrAgt : [
                                                            FinInstnId :[
                                                                    Othr : [
                                                                    	Id : docCdtrAgt
                                                                    ]
                                                            ]
                                                    ],
                                            ],
                                            SplmtryData :[[
                                                    Envlp :[
                                                            Dtl :[
                                                                    Cdtr :[
                                                                            Tp : DocCdtrTp,
                                                                            Id : DocCdtrId,
                                                                            RsdntSts : DocRsdntSts,
                                                                            TwnNm : DocCdtrTwnNm,
                                                                    ],
													   DbtrAgtAcct :[
                                                                            Id : [
                                                                            	Othr : [
                                                                            		Id : "88888888"
                                                                            	]
                                                                            ]
                                                                    ],
													   CdtrAgtAcct :[
                                                                            Id : [
                                                                            	Othr : [
                                                                            		Id : "12312312"
                                                                            	]
                                                                            ]
                                                                    ],                                                                    
                                                            ]
                                                    ]
                                            ]]
                                    ]]

                            ]
                    ]
            ]
    ]
jsonbody = new groovy.json.JsonBuilder() 
jsonbody output
soapRequest = jsonbody.toString()

com.eviware.soapui.SoapUI.globalProperties.setPropertyValue("CIConnRevCTSCReq", soapRequest)	
def soapUrl = new URL("http://10.14.52.240:3022/api/sttlconf")
def connection = soapUrl.openConnection()

def protectedObj = [
	"x5t#s256":"42nzrzb_QkgYU_BIO8Erj2ssNH8B9Dj7PCEvRRHjbYQ",
	alg:"RS256",
	typ:"JWT"
]


def protectedStr = JsonOutput.toJson(protectedObj).replaceAll("\\s", "")
log.warn protectedStr
def encodedProtected = Base64.getUrlEncoder().withoutPadding().encodeToString(protectedStr.getBytes("UTF-8"))//protectedStr.bytes.encodeBase64().toString()//.withoutPadding()	
log.warn "encodedprotected " + encodedProtected

def getPayload = JsonOutput.toJson(output)
log.warn getPayload
def payloadEncoded = Base64.getUrlEncoder().withoutPadding().encodeToString(getPayload.getBytes("UTF-8"))//payloadJson.bytes.encodeBase64().toString()
log.info "payloadencoded "+  payloadEncoded
def setSignature = encodedProtected+"."+payloadEncoded



def loadPrivateKey(String pemFilePath) 
{
    def pemFile = new File(pemFilePath)
    if (!pemFile.exists()) {
        throw new FileNotFoundException("Private key file not found: " + pemFilePath)
    }

    def pem = pemFile.text
    pem = pem.replaceAll("\\r", "").replaceAll("\\n", "") // Normalize line breaks
    pem = pem.replace("-----BEGIN RSA PRIVATE KEY-----", "").replace("-----END RSA PRIVATE KEY-----", "") // Remove headers

    byte[] keyBytes = Base64.getDecoder().decode(pem.trim()) // Decode Base64
    KeyFactory keyFactory = KeyFactory.getInstance("RSA")
    PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(keyBytes)
    log.warn "keyspec " + keySpec

    return keyFactory.generatePrivate(keySpec) // Return PrivateKey object
}


// Sign data using RS256 and encode to Base64-URL
def signWithRS256(PrivateKey privateKey, String data) {
    Signature signer = Signature.getInstance("SHA256withRSA") // Use RS256 Algorithm
    signer.initSign(privateKey)
    signer.update(data.bytes) // Convert string to bytes
    byte[] signature = signer.sign() // Generate signature

    return Base64.getUrlEncoder().withoutPadding().encodeToString(signature) // Base64-URL Encode
}


def privateKeyPath = "E:\\QADocs\\Project 2025\\BIFAST - OSSW\\secret_key.pem"
def originalData = setSignature

// Load private key and sign data
def privateKey = loadPrivateKey(privateKeyPath)
def signedData = signWithRS256(privateKey, originalData)

log.info "Signed Base64-URL Output: " + signedData
def jwtHeaders = encodedProtected + "." + payloadEncoded + "." + signedData

connection.setRequestMethod("POST")
connection.setRequestProperty("Content-Type" ,"application/json")
connection.setRequestProperty("Signature" ,jwtHeaders)
//connection.setRequestProperty("SOAPAction", queryString)
connection.setRequestProperty("Connection", "Close")
connection.setConnectTimeout( 20000 );
connection.setReadTimeout( 20000 );

// Adding the custom header to request headers.
//request.requestHeaders = headers

//connection.setSSLSocketFactory(sslFactory)
connection.doOutput = true

def headers = new StringToStringMap()
headers.put("Signature", jwtHeaders)

Writer writer = new OutputStreamWriter(connection.outputStream);
writer.write(soapRequest)
writer.flush()
writer.close()
connection.connect()

soapResponse = connection.content.text
}