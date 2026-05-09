"""
This module has been based on the output of
the `ffmpeg` codecs that is shown in this
link:
- https://gist.github.com/dougal/160f33aa6f0c38c95b4bf4dbe4732c09
"""
from pystandards.enum import BaseEnum as Enum


class FfmpegVideoCodec(Enum):
    """
    The video códecs supported by `ffmpeg` (if it
    is available or not depends on the `ffmpeg`
    implementation).
    """

    # These below are added because I used them in
    # some personal projects
    LIBX264 = 'libx264'
    """
    The compatibility king (mp4, mov, mvk), almost
    every device.
    """
    LIBX265 = 'libx265'
    """
    Sucessor of H.264 with better compression but
    less compatible (mp4, mkv).
    """
    PRORES_KS = 'prores_ks'
    """
    TODO: Explain it
    """
    H264_NVENC = 'h264_nvenc'
    """
    H.264 but for Nvidia graphic cards.
    """
    LIBVPX_VP9 = 'libvpx-vp9'
    """
    TODO: Explain it
    """
    # These below were extracted from this link:
    # https://gist.github.com/dougal/160f33aa6f0c38c95b4bf4dbe4732c09
    CODEC_012V = "012v"
    """
    Uncompressed 4:2:2 10-bit
    """
    CODEC_4XM = "4xm"
    """
    4X Movie
    """
    CODEC_8BPS = "8bps"
    """
    QuickTime 8BPS video
    """
    A64_MULTI = "a64_multi"
    """
    Multicolor charset for Commodore 64
    """
    A64_MULTI5 = "a64_multi5"
    """
    Multicolor charset for Commodore 64 with 5th color
    """
    AASC = "aasc"
    """
    Autodesk RLE
    """
    AGM = "agm"
    """
    Amuse Graphics Movie
    """
    AIC = "aic"
    """
    Apple Intermediate Codec
    """
    ALIAS_PIX = "alias_pix"
    """
    Alias/Wavefront PIX image
    """
    AMV = "amv"
    """
    AMV Video
    """
    ANM = "anm"
    """
    Deluxe Paint Animation
    """
    ANSI = "ansi"
    """
    ASCII/ANSI art
    """
    APNG = "apng"
    """
    Animated Portable Network Graphics
    """
    ARBC = "arbc"
    """
    Gryphon's Anim Compressor
    """
    ASV1 = "asv1"
    """
    ASUS V1
    """
    ASV2 = "asv2"
    """
    ASUS V2
    """
    AURA = "aura"
    """
    Auravision AURA
    """
    AURA2 = "aura2"
    """
    Auravision Aura 2
    """
    AV1 = "av1"
    """
    Alliance for Open Media AV1
    """
    AVRN = "avrn"
    """
    Avid AVI Codec
    """
    AVRP = "avrp"
    """
    Avid 1:1 10-bit RGB Packer
    """
    AVS = "avs"
    """
    AVS video
    """
    AVS2 = "avs2"
    """
    AVS2-P2 / IEEE1857.4
    """
    AVUI = "avui"
    """
    Avid Meridien Uncompressed
    """
    AYUV = "ayuv"
    """
    Uncompressed packed MS 4:4:4:4
    """
    BETHSOFTVID = "bethsoftvid"
    """
    Bethesda VID video
    """
    BFI = "bfi"
    """
    Brute Force & Ignorance
    """
    BINKVIDEO = "binkvideo"
    """
    Bink video
    """
    BINTEXT = "bintext"
    """
    Binary text
    """
    BITPACKED = "bitpacked"
    """
    Bitpacked video
    """
    BMP = "bmp"
    """
    BMP image
    """
    BMV_VIDEO = "bmv_video"
    """
    Discworld II BMV video
    """
    BRENDER_PIX = "brender_pix"
    """
    BRender PIX image
    """
    C93 = "c93"
    """
    Interplay C93
    """
    CAVS = "cavs"
    """
    Chinese AVS
    """
    CDGRAPHICS = "cdgraphics"
    """
    CD Graphics video
    """
    CDXL = "cdxl"
    """
    Commodore CDXL video
    """
    CFHD = "cfhd"
    """
    Cineform HD
    """
    CINEPAK = "cinepak"
    """
    Cinepak
    """
    CLEARVIDEO = "clearvideo"
    """
    Iterated Systems ClearVideo
    """
    CLJR = "cljr"
    """
    Cirrus Logic AccuPak
    """
    CLLC = "cllc"
    """
    Canopus Lossless Codec
    """
    CMV = "cmv"
    """
    Electronic Arts CMV video
    """
    CPIA = "cpia"
    """
    CPiA video format
    """
    CSCD = "cscd"
    """
    CamStudio
    """
    CYUV = "cyuv"
    """
    Creative YUV
    """
    DAALA = "daala"
    """
    Daala
    """
    DDS = "dds"
    """
    DirectDraw Surface image
    """
    DFA = "dfa"
    """
    Chronomaster DFA
    """
    DIRAC = "dirac"
    """
    Dirac
    """
    DNXHD = "dnxhd"
    """
    VC3 / DNxHD
    """
    DPX = "dpx"
    """
    Digital Picture Exchange image
    """
    DSICINVIDEO = "dsicinvideo"
    """
    Delphine CIN video
    """
    DVVIDEO = "dvvideo"
    """
    DV video
    """
    DXA = "dxa"
    """
    Feeble Files DXA
    """
    DXTORY = "dxtory"
    """
    Dxtory
    """
    DXV = "dxv"
    """
    Resolume DXV
    """
    ESCAPE124 = "escape124"
    """
    Escape 124
    """
    ESCAPE130 = "escape130"
    """
    Escape 130
    """
    EXR = "exr"
    """
    OpenEXR image
    """
    FFV1 = "ffv1"
    """
    FFmpeg video codec #1
    """
    FFVHUFF = "ffvhuff"
    """
    FFmpeg Huffyuv variant
    """
    FIC = "fic"
    """
    Mirillis FIC
    """
    FITS = "fits"
    """
    Flexible Image Transport System
    """
    FLASHSV = "flashsv"
    """
    Flash Screen Video v1
    """
    FLASHSV2 = "flashsv2"
    """
    Flash Screen Video v2
    """
    FLIC = "flic"
    """
    Autodesk Flic
    """
    FLV1 = "flv1"
    """
    Flash Video
    """
    FMVC = "fmvc"
    """
    FM Screen Capture Codec
    """
    FRAPS = "fraps"
    """
    Fraps codec
    """
    FRWU = "frwu"
    """
    Forward Uncompressed
    """
    G2M = "g2m"
    """
    Go2Meeting
    """
    GDV = "gdv"
    """
    Gremlin Digital Video
    """
    GIF = "gif"
    """
    Graphics Interchange Format
    """
    H261 = "h261"
    """
    H.261
    """
    H263 = "h263"
    """
    H.263
    """
    H263I = "h263i"
    """
    Intel H.263
    """
    H263P = "h263p"
    """
    H.263+
    """
    H264 = "h264"
    """
    H.264 / AVC.

    Compatible with almost every device. This one
    has specific implementations like 'libx264'.
    """
    HAP = "hap"
    """
    Vidvox Hap
    """
    HEVC = "hevc"
    """
    H.265 / HEVC
    """
    HNM4VIDEO = "hnm4video"
    """
    HNM 4 video
    """
    HQ_HQA = "hq_hqa"
    """
    Canopus HQ/HQA
    """
    HQX = "hqx"
    """
    Canopus HQX
    """
    HUFFYUV = "huffyuv"
    """
    HuffYUV
    """
    HYMT = "hymt"
    """
    HuffYUV MT
    """
    IDCIN = "idcin"
    """
    id Quake II CIN
    """
    IDF = "idf"
    """
    iCEDraw text
    """
    IFF_ILBM = "iff_ilbm"
    """
    IFF ILBM image
    """
    IMM4 = "imm4"
    """
    Infinity IMM4
    """
    INDEO2 = "indeo2"
    """
    Intel Indeo 2
    """
    INDEO3 = "indeo3"
    """
    Intel Indeo 3
    """
    INDEO4 = "indeo4"
    """
    Intel Indeo 4
    """
    INDEO5 = "indeo5"
    """
    Intel Indeo 5
    """
    INTERPLAYVIDEO = "interplayvideo"
    """
    Interplay MVE video
    """
    JPEG2000 = "jpeg2000"
    """
    JPEG 2000
    """
    JPEGLS = "jpegls"
    """
    JPEG-LS
    """
    JV = "jv"
    """
    Bitmap Brothers JV
    """
    KGV1 = "kgv1"
    """
    Kega Game Video
    """
    KMVC = "kmvc"
    """
    Karl Morton's codec
    """
    LAGARITH = "lagarith"
    """
    Lagarith lossless
    """
    LJPEG = "ljpeg"
    """
    Lossless JPEG
    """
    LOCO = "loco"
    """
    LOCO
    """
    LSCR = "lscr"
    """
    LEAD Screen Capture
    """
    M101 = "m101"
    """
    Matrox Uncompressed SD
    """
    MAD = "mad"
    """
    Electronic Arts Madcow
    """
    MAGICYUV = "magicyuv"
    """
    MagicYUV
    """
    MDEC = "mdec"
    """
    PlayStation MDEC
    """
    MIMIC = "mimic"
    """
    Mimic
    """
    MJPEG = "mjpeg"
    """
    Motion JPEG
    """
    MJPEGB = "mjpegb"
    """
    Apple MJPEG-B
    """
    MMVIDEO = "mmvideo"
    """
    American Laser Games MM Video
    """
    MOTIONPIXELS = "motionpixels"
    """
    Motion Pixels
    """
    MPEG1VIDEO = "mpeg1video"
    """
    MPEG-1 video
    """
    MPEG2VIDEO = "mpeg2video"
    """
    MPEG-2 video
    """
    MPEG4 = "mpeg4"
    """
    MPEG-4 part 2
    """
    MSA1 = "msa1"
    """
    MS ATC Screen
    """
    MSCC = "mscc"
    """
    Mandsoft Screen Capture Codec
    """
    MSMPEG4V1 = "msmpeg4v1"
    """
    Microsoft MPEG-4 v1
    """
    MSMPEG4V2 = "msmpeg4v2"
    """
    Microsoft MPEG-4 v2
    """
    MSMPEG4V3 = "msmpeg4v3"
    """
    Microsoft MPEG-4 v3
    """
    MSRLE = "msrle"
    """
    Microsoft RLE
    """
    MSS1 = "mss1"
    """
    MS Screen 1
    """
    MSS2 = "mss2"
    """
    MS Windows Media Video V9 Screen
    """
    MSVIDEO1 = "msvideo1"
    """
    Microsoft Video 1
    """
    MSZH = "mszh"
    """
    LCL MSZH
    """
    MTS2 = "mts2"
    """
    MS Expression Encoder Screen
    """
    MVC1 = "mvc1"
    """
    Silicon Graphics Motion Video Compressor 1
    """
    MVC2 = "mvc2"
    """
    Silicon Graphics Motion Video Compressor 2
    """
    MWSC = "mwsc"
    """
    MatchWare Screen Capture Codec
    """
    MXPEG = "mxpeg"
    """
    Mobotix MxPEG
    """
    NUV = "nuv"
    """
    NuppelVideo / RTJPEG
    """
    PAF_VIDEO = "paf_video"
    """
    Packed Animation File video
    """
    PAM = "pam"
    """
    Portable AnyMap image
    """
    PBM = "pbm"
    """
    Portable BitMap image
    """
    PCX = "pcx"
    """
    PC Paintbrush image
    """
    PGM = "pgm"
    """
    Portable GrayMap image
    """
    PGMYUV = "pgmyuv"
    """
    Portable GrayMap YUV
    """
    PICTOR = "pictor"
    """
    Pictor / PC Paint
    """
    PIXLET = "pixlet"
    """
    Apple Pixlet
    """
    PNG = "png"
    """
    Portable Network Graphics
    """
    PPM = "ppm"
    """
    Portable PixelMap image
    """
    PRORES = "prores"
    """
    Apple ProRes
    """
    PROSUMER = "prosumer"
    """
    Brooktree ProSumer Video
    """
    PSD = "psd"
    """
    Photoshop PSD
    """
    PTX = "ptx"
    """
    V.Flash PTX image
    """
    QDRAW = "qdraw"
    """
    Apple QuickDraw
    """
    QPEG = "qpeg"
    """
    Q-team QPEG
    """
    QTRLE = "qtrle"
    """
    QuickTime Animation RLE, supporting alpha (.mov).
    """
    R10K = "r10k"
    """
    AJA Kona 10-bit RGB
    """
    R210 = "r210"
    """
    Uncompressed RGB 10-bit
    """
    RASC = "rasc"
    """
    RemotelyAnywhere Screen Capture
    """
    RAWVIDEO = "rawvideo"
    """
    Raw video
    """
    RL2 = "rl2"
    """
    RL2 video
    """
    ROQ = "roq"
    """
    id RoQ video
    """
    RPZA = "rpza"
    """
    QuickTime RPZA
    """
    RSCC = "rscc"
    """
    Rsupport Screen Capture Codec
    """
    RV10 = "rv10"
    """
    RealVideo 1.0
    """
    RV20 = "rv20"
    """
    RealVideo 2.0
    """
    RV30 = "rv30"
    """
    RealVideo 3.0
    """
    RV40 = "rv40"
    """
    RealVideo 4.0
    """
    SANM = "sanm"
    """
    LucasArts SANM / SMUSH
    """
    SCPR = "scpr"
    """
    ScreenPressor
    """
    SCREENPRESSO = "screenpresso"
    """
    Screenpresso codec
    """
    SGI = "sgi"
    """
    SGI image
    """
    SGIRLE = "sgirle"
    """
    SGI RLE 8-bit
    """
    SHEERVIDEO = "sheervideo"
    """
    BitJazz SheerVideo
    """
    SMACKVIDEO = "smackvideo"
    """
    Smacker video
    """
    SMC = "smc"
    """
    QuickTime Graphics
    """
    SMVJPEG = "smvjpeg"
    """
    Sigmatel Motion Video JPEG
    """
    SNOW = "snow"
    """
    Snow codec
    """
    SP5X = "sp5x"
    """
    Sunplus JPEG
    """
    SPEEDHQ = "speedhq"
    """
    NewTek SpeedHQ
    """
    SRGC = "srgc"
    """
    Screen Recorder Gold Codec
    """
    SUNRAST = "sunrast"
    """
    Sun Rasterfile image
    """
    SVG = "svg"
    """
    Scalable Vector Graphics
    """
    SVQ1 = "svq1"
    """
    Sorenson Video 1
    """
    SVQ3 = "svq3"
    """
    Sorenson Video 3
    """
    TARGA = "targa"
    """
    Truevision Targa
    """
    TARGA_Y216 = "targa_y216"
    """
    Pinnacle TARGA CineWave YUV16
    """
    TDSC = "tdsc"
    """
    TDSC codec
    """
    TGQ = "tgq"
    """
    Electronic Arts TGQ
    """
    TGV = "tgv"
    """
    Electronic Arts TGV
    """
    THEORA = "theora"
    """
    Theora
    """
    THP = "thp"
    """
    Nintendo Gamecube THP
    """
    TIERTEXSEQVIDEO = "tiertexseqvideo"
    """
    Tiertex SEQ video
    """
    TIFF = "tiff"
    """
    TIFF image
    """
    TMV = "tmv"
    """
    8088flex TMV
    """
    TQI = "tqi"
    """
    Electronic Arts TQI
    """
    TRUEMOTION1 = "truemotion1"
    """
    Duck TrueMotion 1.0
    """
    TRUEMOTION2 = "truemotion2"
    """
    Duck TrueMotion 2.0
    """
    TRUEMOTION2RT = "truemotion2rt"
    """
    Duck TrueMotion 2 Real Time
    """
    TSCC = "tscc"
    """
    TechSmith Screen Capture Codec
    """
    TSCC2 = "tscc2"
    """
    TechSmith Screen Codec 2
    """
    TXD = "txd"
    """
    RenderWare TXD
    """
    ULTI = "ulti"
    """
    IBM UltiMotion
    """
    UTVIDEO = "utvideo"
    """
    Ut Video
    """
    V210 = "v210"
    """
    Uncompressed 4:2:2 10-bit
    """
    V210X = "v210x"
    """
    Uncompressed 4:2:2 10-bit
    """
    V308 = "v308"
    """
    Uncompressed packed 4:4:4
    """
    V408 = "v408"
    """
    Uncompressed QT 4:4:4:4
    """
    V410 = "v410"
    """
    Uncompressed 4:4:4 10-bit
    """
    VB = "vb"
    """
    Beam Software VB
    """
    VBLE = "vble"
    """
    VBLE Lossless Codec
    """
    VC1 = "vc1"
    """
    SMPTE VC-1
    """
    VC1IMAGE = "vc1image"
    """
    Windows Media Video 9 Image
    """
    VCR1 = "vcr1"
    """
    ATI VCR1
    """
    VIXL = "vixl"
    """
    Miro VideoXL
    """
    VMDVIDEO = "vmdvideo"
    """
    Sierra VMD video
    """
    VMNC = "vmnc"
    """
    VMware Screen Codec
    """
    VP3 = "vp3"
    """
    On2 VP3
    """
    VP4 = "vp4"
    """
    On2 VP4
    """
    VP5 = "vp5"
    """
    On2 VP5
    """
    VP6 = "vp6"
    """
    On2 VP6
    """
    VP6A = "vp6a"
    """
    On2 VP6 with alpha
    """
    VP6F = "vp6f"
    """
    On2 VP6 Flash
    """
    VP7 = "vp7"
    """
    On2 VP7
    """
    VP8 = "vp8"
    """
    On2 VP8
    """
    VP9 = "vp9"
    """
    Google VP9
    """
    WCMV = "wcmv"
    """
    WinCAM Motion Video
    """
    WEBP = "webp"
    """
    WebP
    """
    WMV1 = "wmv1"
    """
    Windows Media Video 7
    """
    WMV2 = "wmv2"
    """
    Windows Media Video 8
    """
    WMV3 = "wmv3"
    """
    Windows Media Video 9
    """
    WMV3IMAGE = "wmv3image"
    """
    Windows Media Video 9 Image
    """
    WNV1 = "wnv1"
    """
    Winnov WNV1
    """
    WRAPPED_AVFRAME = "wrapped_avframe"
    """
    AVFrame passthrough
    """
    WS_VQA = "ws_vqa"
    """
    Westwood VQA
    """
    XAN_WC3 = "xan_wc3"
    """
    Wing Commander III Xan
    """
    XAN_WC4 = "xan_wc4"
    """
    Wing Commander IV Xan
    """
    XBIN = "xbin"
    """
    Extended Binary text
    """
    XBM = "xbm"
    """
    X BitMap image
    """
    XFACE = "xface"
    """
    X-Face image
    """
    XPM = "xpm"
    """
    X PixMap image
    """
    XWD = "xwd"
    """
    X Window Dump image
    """
    Y41P = "y41p"
    """
    Uncompressed YUV 4:1:1 12-bit
    """
    YLC = "ylc"
    """
    YUY2 Lossless Codec
    """
    YOP = "yop"
    """
    Psygnosis YOP Video
    """
    YUV4 = "yuv4"
    """
    Uncompressed packed 4:2:0
    """
    ZEROCODEC = "zerocodec"
    """
    ZeroCodec Lossless Video
    """
    ZLIB = "zlib"
    """
    LCL ZLIB
    """
    ZMBV = "zmbv"
    """
    Zip Motion Blocks Video
    """

class FfmpegAudioCodec(Enum):
    """
    The audio códecs supported by `ffmpeg` (if it
    is available or not depends on the `ffmpeg`
    implementation).
    """

    # These below are added because I used them in
    # some personal projects
    MP3FLOAT = 'mp3float'
    """
    Very popular, as float.
    """
    # These below were extracted from this link:
    # https://gist.github.com/dougal/160f33aa6f0c38c95b4bf4dbe4732c09
    AUDIO_4GV = "4gv"
    """
    4GV (Fourth Generation Vocoder)
    """
    AUDIO_8SVX_EXP = "8svx_exp"
    """
    8SVX exponential
    """
    AUDIO_8SVX_FIB = "8svx_fib"
    """
    8SVX fibonacci
    """
    AAC = "aac"
    """
    Advanced Audio Coding (AAC).

    The current standard for video (mp4, mov, mvk)
    with maximum compatibility.
    """
    AAC_LATM = "aac_latm"
    """
    AAC LATM (Low-overhead MPEG-4 Audio Transport Multiplex)
    """
    AC3 = "ac3"
    """
    ATSC A/52A (AC-3)
    """
    ADPCM_4XM = "adpcm_4xm"
    """
    ADPCM 4X Movie
    """
    ADPCM_ADX = "adpcm_adx"
    """
    SEGA CRI ADX ADPCM
    """
    ADPCM_AFC = "adpcm_afc"
    """
    Nintendo Gamecube AFC ADPCM
    """
    ADPCM_AGM = "adpcm_agm"
    """
    AmuseGraphics Movie ADPCM
    """
    ADPCM_AICA = "adpcm_aica"
    """
    Yamaha AICA ADPCM
    """
    ADPCM_CT = "adpcm_ct"
    """
    Creative Technology ADPCM
    """
    ADPCM_DTK = "adpcm_dtk"
    """
    Nintendo Gamecube DTK ADPCM
    """
    ADPCM_EA = "adpcm_ea"
    """
    Electronic Arts ADPCM
    """
    ADPCM_EA_MAXIS_XA = "adpcm_ea_maxis_xa"
    """
    EA Maxis CDROM XA ADPCM
    """
    ADPCM_EA_R1 = "adpcm_ea_r1"
    """
    Electronic Arts R1 ADPCM
    """
    ADPCM_EA_R2 = "adpcm_ea_r2"
    """
    Electronic Arts R2 ADPCM
    """
    ADPCM_EA_R3 = "adpcm_ea_r3"
    """
    Electronic Arts R3 ADPCM
    """
    ADPCM_EA_XAS = "adpcm_ea_xas"
    """
    Electronic Arts XAS ADPCM
    """
    ADPCM_G722 = "adpcm_g722"
    """
    G.722 ADPCM
    """
    ADPCM_G726 = "adpcm_g726"
    """
    G.726 ADPCM
    """
    ADPCM_G726LE = "adpcm_g726le"
    """
    G.726 little-endian ADPCM
    """
    ADPCM_IMA_AMV = "adpcm_ima_amv"
    """
    IMA ADPCM AMV
    """
    ADPCM_IMA_APC = "adpcm_ima_apc"
    """
    IMA ADPCM CRYO APC
    """
    ADPCM_IMA_DAT4 = "adpcm_ima_dat4"
    """
    IMA ADPCM Eurocom DAT4
    """
    ADPCM_IMA_DK3 = "adpcm_ima_dk3"
    """
    IMA ADPCM Duck DK3
    """
    ADPCM_IMA_DK4 = "adpcm_ima_dk4"
    """
    IMA ADPCM Duck DK4
    """
    ADPCM_IMA_EA_EACS = "adpcm_ima_ea_eacs"
    """
    IMA ADPCM EA EACS
    """
    ADPCM_IMA_EA_SEAD = "adpcm_ima_ea_sead"
    """
    IMA ADPCM EA SEAD
    """
    ADPCM_IMA_ISS = "adpcm_ima_iss"
    """
    IMA ADPCM Funcom ISS
    """
    ADPCM_IMA_OKI = "adpcm_ima_oki"
    """
    IMA ADPCM OKI
    """
    ADPCM_IMA_QT = "adpcm_ima_qt"
    """
    IMA ADPCM QuickTime
    """
    ADPCM_IMA_RAD = "adpcm_ima_rad"
    """
    IMA ADPCM Radical
    """
    ADPCM_IMA_SMJPEG = "adpcm_ima_smjpeg"
    """
    IMA ADPCM Loki SMJPEG
    """
    ADPCM_IMA_WAV = "adpcm_ima_wav"
    """
    IMA ADPCM WAV
    """
    ADPCM_IMA_WS = "adpcm_ima_ws"
    """
    IMA ADPCM Westwood
    """
    ADPCM_MS = "adpcm_ms"
    """
    Microsoft ADPCM
    """
    ADPCM_MTAF = "adpcm_mtaf"
    """
    MTAF ADPCM
    """
    ADPCM_PSX = "adpcm_psx"
    """
    PlayStation ADPCM
    """
    ADPCM_SBPRO_2 = "adpcm_sbpro_2"
    """
    Sound Blaster Pro 2-bit ADPCM
    """
    ADPCM_SBPRO_3 = "adpcm_sbpro_3"
    """
    Sound Blaster Pro 2.6-bit ADPCM
    """
    ADPCM_SBPRO_4 = "adpcm_sbpro_4"
    """
    Sound Blaster Pro 4-bit ADPCM
    """
    ADPCM_SWF = "adpcm_swf"
    """
    Shockwave Flash ADPCM
    """
    ADPCM_THP = "adpcm_thp"
    """
    Nintendo THP ADPCM
    """
    ADPCM_THP_LE = "adpcm_thp_le"
    """
    Nintendo THP ADPCM little-endian
    """
    ADPCM_VIMA = "adpcm_vima"
    """
    LucasArts VIMA ADPCM
    """
    ADPCM_XA = "adpcm_xa"
    """
    CD-ROM XA ADPCM
    """
    ADPCM_YAMAHA = "adpcm_yamaha"
    """
    Yamaha ADPCM
    """
    ALAC = "alac"
    """
    Apple Lossless Audio Codec
    """
    AMR_NB = "amr_nb"
    """
    Adaptive Multi-Rate Narrowband
    """
    AMR_WB = "amr_wb"
    """
    Adaptive Multi-Rate Wideband
    """
    APE = "ape"
    """
    Monkey’s Audio lossless
    """
    ATRAC1 = "atrac1"
    """
    ATRAC1
    """
    ATRAC3 = "atrac3"
    """
    ATRAC3
    """
    ATRAC3AL = "atrac3al"
    """
    ATRAC3 Advanced Lossless
    """
    ATRAC3P = "atrac3p"
    """
    ATRAC3+
    """
    ATRAC3PAL = "atrac3pal"
    """
    ATRAC3+ Advanced Lossless
    """
    ATRAC9 = "atrac9"
    """
    ATRAC9
    """
    AVC_AUDIO = "avc"
    """
    On2 Audio for Video Codec
    """
    BINKAUDIO_DCT = "binkaudio_dct"
    """
    Bink Audio DCT
    """
    BINKAUDIO_RDFT = "binkaudio_rdft"
    """
    Bink Audio RDFT
    """
    BMV_AUDIO = "bmv_audio"
    """
    Discworld II BMV audio
    """
    CELT = "celt"
    """
    Constrained Energy Lapped Transform
    """
    CODEC2 = "codec2"
    """
    Very low bitrate speech codec
    """
    COMFORTNOISE = "comfortnoise"
    """
    RFC 3389 Comfort Noise
    """
    COOK = "cook"
    """
    Cook / RealAudio G2
    """
    DOLBY_E = "dolby_e"
    """
    Dolby E
    """
    DSD_LSBF = "dsd_lsbf"
    """
    DSD least-significant-bit first
    """
    DSD_LSBF_PLANAR = "dsd_lsbf_planar"
    """
    DSD LSBF planar
    """
    DSD_MSBF = "dsd_msbf"
    """
    DSD most-significant-bit first
    """
    DSD_MSBF_PLANAR = "dsd_msbf_planar"
    """
    DSD MSBF planar
    """
    DSICINAUDIO = "dsicinaudio"
    """
    Delphine CIN audio
    """
    DSS_SP = "dss_sp"
    """
    Digital Speech Standard SP
    """
    DST = "dst"
    """
    Direct Stream Transfer
    """
    DTS = "dts"
    """
    DCA DTS Coherent Acoustics
    """
    DVAUDIO = "dvaudio"
    """
    DV audio
    """
    EAC3 = "eac3"
    """
    Enhanced AC-3
    """
    EVRC = "evrc"
    """
    Enhanced Variable Rate Codec
    """
    FLAC = "flac"
    """
    Free Lossless Audio Codec
    """
    G723_1 = "g723_1"
    """
    ITU G.723.1
    """
    G729 = "g729"
    """
    ITU G.729
    """
    GREMLIN_DPCM = "gremlin_dpcm"
    """
    Gremlin DPCM
    """
    GSM = "gsm"
    """
    GSM Full Rate
    """
    GSM_MS = "gsm_ms"
    """
    GSM Microsoft variant
    """
    HCOM = "hcom"
    """
    HCOM Audio
    """
    IAC = "iac"
    """
    Indeo Audio Coder
    """
    ILBC = "ilbc"
    """
    Internet Low Bitrate Codec
    """
    IMC = "imc"
    """
    Intel Music Coder
    """
    INTERPLAY_DPCM = "interplay_dpcm"
    """
    Interplay DPCM
    """
    INTERPLAYACM = "interplayacm"
    """
    Interplay ACM
    """
    MACE3 = "mace3"
    """
    MACE 3:1
    """
    MACE6 = "mace6"
    """
    MACE 6:1
    """
    METASOUND = "metasound"
    """
    Voxware MetaSound
    """
    MLP = "mlp"
    """
    Meridian Lossless Packing
    """
    MP1 = "mp1"
    """
    MPEG Audio Layer I
    """
    MP2 = "mp2"
    """
    MPEG Audio Layer II
    """
    MP3 = "mp3"
    """
    MPEG Audio Layer III.

    Very popular in music but less used than aac or
    opus.
    """
    MP3ADU = "mp3adu"
    """
    ADU MP3 (Application Data Unit MPEG Layer III)
    """
    MP3ON4 = "mp3on4"
    """
    MP3 on MP4
    """
    MP4ALS = "mp4als"
    """
    MPEG-4 Audio Lossless Coding
    """
    MUSEPACK7 = "musepack7"
    """
    Musepack SV7
    """
    MUSEPACK8 = "musepack8"
    """
    Musepack SV8
    """
    NELLYMOSER = "nellymoser"
    """
    Nellymoser Asao codec
    """
    OPUS = "opus"
    """
    Opus Interactive Audio Codec.

    Excellent quality with low bitrate. Modern 
    standard in WebM, streaming and VoIP.
    """
    PAF_AUDIO = "paf_audio"
    """
    Amazing Studio Packed Animation File audio
    """
    PCM_ALAW = "pcm_alaw"
    """
    PCM A-law / G.711 A-law
    """
    PCM_BLURAY = "pcm_bluray"
    """
    PCM signed 16/20/24-bit big-endian for Blu-ray
    """
    PCM_DVD = "pcm_dvd"
    """
    PCM signed 20/24-bit big-endian for DVD
    """
    PCM_F16LE = "pcm_f16le"
    """
    PCM 16.8 floating point little-endian
    """
    PCM_F24LE = "pcm_f24le"
    """
    PCM 24-bit floating point little-endian
    """
    PCM_F32BE = "pcm_f32be"
    """
    PCM 32-bit floating point big-endian
    """
    PCM_F32LE = "pcm_f32le"
    """
    PCM 32-bit floating point little-endian
    """
    PCM_F64BE = "pcm_f64be"
    """
    PCM 64-bit floating point big-endian
    """
    PCM_F64LE = "pcm_f64le"
    """
    PCM 64-bit floating point little-endian
    """
    PCM_LXF = "pcm_lxf"
    """
    PCM signed 20-bit little-endian planar
    """
    PCM_MULAW = "pcm_mulaw"
    """
    PCM mu-law / G.711 mu-law
    """
    PCM_S16BE = "pcm_s16be"
    """
    PCM signed 16-bit big-endian
    """
    PCM_S16BE_PLANAR = "pcm_s16be_planar"
    """
    PCM signed 16-bit big-endian planar
    """
    PCM_S16LE = "pcm_s16le"
    """
    PCM signed 16-bit little-endian
    """
    PCM_S16LE_PLANAR = "pcm_s16le_planar"
    """
    PCM signed 16-bit little-endian planar
    """
    PCM_S24BE = "pcm_s24be"
    """
    PCM signed 24-bit big-endian
    """
    PCM_S24DAUD = "pcm_s24daud"
    """
    PCM D-Cinema signed 24-bit audio
    """
    PCM_S24LE = "pcm_s24le"
    """
    PCM signed 24-bit little-endian
    """
    PCM_S24LE_PLANAR = "pcm_s24le_planar"
    """
    PCM signed 24-bit little-endian planar
    """
    PCM_S32BE = "pcm_s32be"
    """
    PCM signed 32-bit big-endian
    """
    PCM_S32LE = "pcm_s32le"
    """
    PCM signed 32-bit little-endian
    """
    PCM_S32LE_PLANAR = "pcm_s32le_planar"
    """
    PCM signed 32-bit little-endian planar
    """
    PCM_S64BE = "pcm_s64be"
    """
    PCM signed 64-bit big-endian
    """
    PCM_S64LE = "pcm_s64le"
    """
    PCM signed 64-bit little-endian
    """
    PCM_S8 = "pcm_s8"
    """
    PCM signed 8-bit
    """
    PCM_S8_PLANAR = "pcm_s8_planar"
    """
    PCM signed 8-bit planar
    """
    PCM_U16BE = "pcm_u16be"
    """
    PCM unsigned 16-bit big-endian
    """
    PCM_U16LE = "pcm_u16le"
    """
    PCM unsigned 16-bit little-endian
    """
    PCM_U24BE = "pcm_u24be"
    """
    PCM unsigned 24-bit big-endian
    """
    PCM_U24LE = "pcm_u24le"
    """
    PCM unsigned 24-bit little-endian
    """
    PCM_U32BE = "pcm_u32be"
    """
    PCM unsigned 32-bit big-endian
    """
    PCM_U32LE = "pcm_u32le"
    """
    PCM unsigned 32-bit little-endian
    """
    PCM_U8 = "pcm_u8"
    """
    PCM unsigned 8-bit
    """
    PCM_VIDC = "pcm_vidc"
    """
    PCM Archimedes VIDC
    """
    PCM_ZORK = "pcm_zork"
    """
    PCM Zork
    """
    QCELP = "qcelp"
    """
    QCELP / PureVoice
    """
    QDM2 = "qdm2"
    """
    QDesign Music Codec 2
    """
    QDMC = "qdmc"
    """
    QDesign Music
    """
    RA_144 = "ra_144"
    """
    RealAudio 1.0 (14.4K)
    """
    RA_288 = "ra_288"
    """
    RealAudio 2.0 (28.8K)
    """
    RALF = "ralf"
    """
    RealAudio Lossless
    """
    ROQ_DPCM = "roq_dpcm"
    """
    DPCM id RoQ
    """
    S302M = "s302m"
    """
    SMPTE 302M audio
    """
    SBC = "sbc"
    """
    Low-complexity Subband Codec
    """
    SDX2_DPCM = "sdx2_dpcm"
    """
    DPCM Squareroot-Delta-Exact
    """
    SHORTEN = "shorten"
    """
    Shorten lossless audio codec
    """
    SIPR = "sipr"
    """
    RealAudio SIPR / ACELP.NET
    """
    SMACKAUDIO = "smackaudio"
    """
    Smacker audio
    """
    SMV = "smv"
    """
    Selectable Mode Vocoder
    """
    SOL_DPCM = "sol_dpcm"
    """
    DPCM Sol
    """
    SONIC = "sonic"
    """
    Sonic audio codec
    """
    SONICLS = "sonicls"
    """
    Sonic lossless
    """
    SPEEX = "speex"
    """
    Speex speech codec
    """
    TAK = "tak"
    """
    Tom's lossless Audio Kompressor
    """
    TRUEHD = "truehd"
    """
    Dolby TrueHD
    """
    TRUESPEECH = "truespeech"
    """
    DSP Group TrueSpeech
    """
    TTA = "tta"
    """
    True Audio
    """
    TWINVQ = "twinvq"
    """
    TwinVQ / VQF
    """
    VMDAUDIO = "vmdaudio"
    """
    Sierra VMD audio
    """
    VORBIS = "vorbis"
    """
    Xiph Vorbis
    """
    WAVESYNTH = "wavesynth"
    """
    Wave synthesis pseudo-codec
    """
    WAVPACK = "wavpack"
    """
    WavPack
    """
    WESTWOOD_SND1 = "westwood_snd1"
    """
    Westwood Audio SND1
    """
    WMALOSSLESS = "wmalossless"
    """
    Windows Media Audio Lossless
    """
    WMAPRO = "wmapro"
    """
    Windows Media Audio 9 Professional
    """
    WMAV1 = "wmav1"
    """
    Windows Media Audio 1
    """
    WMAV2 = "wmav2"
    """
    Windows Media Audio 2
    """
    WMAVOICE = "wmavoice"
    """
    Windows Media Audio Voice
    """
    XAN_DPCM = "xan_dpcm"
    """
    DPCM Xan
    """
    XMA1 = "xma1"
    """
    Xbox Media Audio 1
    """
    XMA2 = "xma2"
    """
    Xbox Media Audio 2
    """


# TODO: Add 'FfmpegAudioFormat'
# TODO: Add 'FfmpegVideoFormat'