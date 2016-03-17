/* A Bison parser, made by GNU Bison 3.0.2.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2013 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "3.0.2"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* Copy the first part of user declarations.  */
#line 19 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:339  */

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "sip.h"


#define MAX_NESTED_IF       10
#define MAX_NESTED_SCOPE    10

#define inMainModule()      (currentSpec->module == currentModule || currentModule->container != NULL)


static sipSpec *currentSpec;            /* The current spec being parsed. */
static stringList *backstops;           /* The list of backstops. */
static stringList *neededQualifiers;    /* The list of required qualifiers. */
static stringList *excludedQualifiers;  /* The list of excluded qualifiers. */
static moduleDef *currentModule;        /* The current module being parsed. */
static mappedTypeDef *currentMappedType;    /* The current mapped type. */
static enumDef *currentEnum;            /* The current enum being parsed. */
static int sectionFlags;                /* The current section flags. */
static int currentOverIsVirt;           /* Set if the overload is virtual. */
static int currentCtorIsExplicit;       /* Set if the ctor is explicit. */
static int currentIsStatic;             /* Set if the current is static. */
static int currentIsSignal;             /* Set if the current is Q_SIGNAL. */
static int currentIsSlot;               /* Set if the current is Q_SLOT. */
static int currentIsTemplate;           /* Set if the current is a template. */
static char *previousFile;              /* The file just parsed. */
static parserContext currentContext;    /* The current context. */
static int skipStackPtr;                /* The skip stack pointer. */
static int skipStack[MAX_NESTED_IF];    /* Stack of skip flags. */
static classDef *scopeStack[MAX_NESTED_SCOPE];  /* The scope stack. */
static int sectFlagsStack[MAX_NESTED_SCOPE];    /* The section flags stack. */
static int currentScopeIdx;             /* The scope stack index. */
static int currentTimelineOrder;        /* The current timeline order. */
static classList *currentSupers;        /* The current super-class list. */
static KwArgs defaultKwArgs;            /* The default keyword arguments support. */
static int makeProtPublic;              /* Treat protected items as public. */
static int parsingCSignature;           /* An explicit C/C++ signature is being parsed. */


static const char *getPythonName(moduleDef *mod, optFlags *optflgs,
        const char *cname);
static classDef *findClass(sipSpec *pt, ifaceFileType iftype,
        apiVersionRangeDef *api_range, scopedNameDef *fqname);
static classDef *findClassWithInterface(sipSpec *pt, ifaceFileDef *iff);
static classDef *newClass(sipSpec *pt, ifaceFileType iftype,
        apiVersionRangeDef *api_range, scopedNameDef *snd,
        const char *virt_error_handler, typeHintDef *typehint_in,
        typeHintDef *typehint_out, const char *typehint_value);
static void finishClass(sipSpec *, moduleDef *, classDef *, optFlags *);
static exceptionDef *findException(sipSpec *pt, scopedNameDef *fqname, int new);
static mappedTypeDef *newMappedType(sipSpec *,argDef *, optFlags *);
static enumDef *newEnum(sipSpec *pt, moduleDef *mod, mappedTypeDef *mt_scope,
        char *name, optFlags *of, int flags);
static void instantiateClassTemplate(sipSpec *pt, moduleDef *mod,
        classDef *scope, scopedNameDef *fqname, classTmplDef *tcd,
        templateDef *td, const char *pyname);
static void newTypedef(sipSpec *, moduleDef *, char *, argDef *, optFlags *);
static void newVar(sipSpec *pt, moduleDef *mod, char *name, int isstatic,
        argDef *type, optFlags *of, codeBlock *acode, codeBlock *gcode,
        codeBlock *scode, int section);
static void newCtor(moduleDef *, char *, int, signatureDef *, optFlags *,
        codeBlock *, throwArgs *, signatureDef *, int, codeBlock *);
static void newFunction(sipSpec *, moduleDef *, classDef *, mappedTypeDef *,
        int, int, int, int, int, char *, signatureDef *, int, int, optFlags *,
        codeBlock *, codeBlock *, codeBlock *, throwArgs *, signatureDef *,
        codeBlock *);
static optFlag *findOptFlag(optFlags *flgs, const char *name);
static optFlag *getOptFlag(optFlags *flgs, const char *name, flagType ft);
static memberDef *findFunction(sipSpec *, moduleDef *, classDef *,
        mappedTypeDef *, const char *, int, int, int);
static void checkAttributes(sipSpec *, moduleDef *, classDef *,
        mappedTypeDef *, const char *, int);
static void newModule(FILE *fp, const char *filename);
static moduleDef *allocModule();
static void parseFile(FILE *fp, const char *name, moduleDef *prevmod,
        int optional);
static void handleEOF(void);
static void handleEOM(void);
static qualDef *findQualifier(const char *name);
static const char *getInt(const char *cp, int *ip);
static scopedNameDef *text2scopedName(ifaceFileDef *scope, char *text);
static scopedNameDef *scopeScopedName(ifaceFileDef *scope,
        scopedNameDef *name);
static void pushScope(classDef *);
static void popScope(void);
static classDef *currentScope(void);
static void newQualifier(moduleDef *, int, int, int, const char *, qualType);
static qualDef *allocQualifier(moduleDef *, int, int, int, const char *,
        qualType);
static void newImport(const char *filename);
static int timePeriod(const char *lname, const char *uname);
static int platOrFeature(char *,int);
static int notSkipping(void);
static void getHooks(optFlags *,char **,char **);
static int getTransfer(optFlags *optflgs);
static int getReleaseGIL(optFlags *optflgs);
static int getHoldGIL(optFlags *optflgs);
static int getDeprecated(optFlags *optflgs);
static int getAllowNone(optFlags *optflgs);
static int getDisallowNone(optFlags *optflgs);
static const char *getVirtErrorHandler(optFlags *optflgs);
static const char *getDocType(optFlags *optflgs);
static const char *getTypeHintValue(optFlags *optflgs);
static void getTypeHints(optFlags *optflgs, typeHintDef **in,
        typeHintDef **out);
static int getNoTypeHint(optFlags *optflgs);
static void templateSignature(signatureDef *sd, int result, classTmplDef *tcd,
        templateDef *td, classDef *ncd, scopedNameDef *type_names,
        scopedNameDef *type_values);
static void templateType(argDef *ad, classTmplDef *tcd, templateDef *td,
        classDef *ncd, scopedNameDef *type_names, scopedNameDef *type_values);
static int search_back(const char *end, const char *start, const char *target);
static char *type2string(argDef *ad);
static char *scopedNameToString(scopedNameDef *name);
static void addUsedFromCode(sipSpec *pt, ifaceFileList **used, const char *sname);
static int sameName(scopedNameDef *snd, const char *sname);
static int stringFind(stringList *sl, const char *s);
static void setModuleName(sipSpec *pt, moduleDef *mod, const char *fullname);
static int foundInScope(scopedNameDef *fq_name, scopedNameDef *rel_name);
static void defineClass(scopedNameDef *snd, classList *supers, optFlags *of);
static classDef *completeClass(scopedNameDef *snd, optFlags *of, int has_def);
static memberDef *instantiateTemplateMethods(memberDef *tmd, moduleDef *mod);
static void instantiateTemplateEnums(sipSpec *pt, classTmplDef *tcd,
        templateDef *td, classDef *cd, ifaceFileList **used,
        scopedNameDef *type_names, scopedNameDef *type_values);
static void instantiateTemplateVars(sipSpec *pt, classTmplDef *tcd,
        templateDef *td, classDef *cd, ifaceFileList **used,
        scopedNameDef *type_names, scopedNameDef *type_values);
static void instantiateTemplateTypedefs(sipSpec *pt, classTmplDef *tcd,
        templateDef *td, classDef *cd, scopedNameDef *type_names,
        scopedNameDef *type_values);
static overDef *instantiateTemplateOverloads(sipSpec *pt, overDef *tod,
        memberDef *tmethods, memberDef *methods, classTmplDef *tcd,
        templateDef *td, classDef *cd, ifaceFileList **used,
        scopedNameDef *type_names, scopedNameDef *type_values);
static void resolveAnyTypedef(sipSpec *pt, argDef *ad);
static void addTypedef(sipSpec *pt, typedefDef *tdd);
static void addVariable(sipSpec *pt, varDef *vd);
static void applyTypeFlags(moduleDef *mod, argDef *ad, optFlags *flags);
static Format convertFormat(const char *format);
static argType convertEncoding(const char *encoding);
static apiVersionRangeDef *getAPIRange(optFlags *optflgs);
static apiVersionRangeDef *convertAPIRange(moduleDef *mod, nameDef *name,
        int from, int to);
static char *convertFeaturedString(char *fs);
static scopedNameDef *text2scopePart(char *text);
static KwArgs keywordArgs(moduleDef *mod, optFlags *optflgs, signatureDef *sd,
        int need_name);
static char *strip(char *s);
static int isEnabledFeature(const char *name);
static void addProperty(sipSpec *pt, moduleDef *mod, classDef *cd,
        const char *name, const char *get, const char *set,
        codeBlock *docstring);
static moduleDef *configureModule(sipSpec *pt, moduleDef *module,
        const char *filename, const char *name, int version, int c_module,
        KwArgs kwargs, int use_arg_names, int call_super_init,
        int all_raise_py_exc, const char *def_error_handler,
        codeBlock *docstring);
static void addAutoPyName(moduleDef *mod, const char *remove_leading);
static KwArgs convertKwArgs(const char *kwargs);
static void checkAnnos(optFlags *annos, const char *valid[]);
static void checkNoAnnos(optFlags *annos, const char *msg);
static void appendCodeBlock(codeBlockList **headp, codeBlock *cb);
static void handleKeepReference(optFlags *optflgs, argDef *ad, moduleDef *mod);
static void mappedTypeAnnos(mappedTypeDef *mtd, optFlags *optflgs);
static void add_new_deref(argDef *new, argDef *orig, int isconst);
static void add_derefs(argDef *dst, argDef *src);
static int isBackstop(qualDef *qd);
static void checkEllipsis(signatureDef *sd);

#line 240 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:339  */

# ifndef YY_NULLPTR
#  if defined __cplusplus && 201103L <= __cplusplus
#   define YY_NULLPTR nullptr
#  else
#   define YY_NULLPTR 0
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* In a future release of Bison, this section will be replaced
   by #include "parser.h".  */
#ifndef YY_YY_HOME_BOB_HG_SIP_SIP_4_18_SNAPSHOT_A4F8A7810CC3_SIPGEN_PARSER_H_INCLUDED
# define YY_YY_HOME_BOB_HG_SIP_SIP_4_18_SNAPSHOT_A4F8A7810CC3_SIPGEN_PARSER_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    TK_API = 258,
    TK_AUTOPYNAME = 259,
    TK_DEFDOCSTRING = 260,
    TK_DEFENCODING = 261,
    TK_PLUGIN = 262,
    TK_VIRTERRORHANDLER = 263,
    TK_EXPTYPEHINTCODE = 264,
    TK_TYPEHINTCODE = 265,
    TK_DOCSTRING = 266,
    TK_DOC = 267,
    TK_EXPORTEDDOC = 268,
    TK_EXTRACT = 269,
    TK_MAKEFILE = 270,
    TK_ACCESSCODE = 271,
    TK_GETCODE = 272,
    TK_SETCODE = 273,
    TK_PREINITCODE = 274,
    TK_INITCODE = 275,
    TK_POSTINITCODE = 276,
    TK_FINALCODE = 277,
    TK_UNITCODE = 278,
    TK_UNITPOSTINCLUDECODE = 279,
    TK_MODCODE = 280,
    TK_TYPECODE = 281,
    TK_PREPYCODE = 282,
    TK_COPYING = 283,
    TK_MAPPEDTYPE = 284,
    TK_CODELINE = 285,
    TK_IF = 286,
    TK_END = 287,
    TK_NAME_VALUE = 288,
    TK_PATH_VALUE = 289,
    TK_STRING_VALUE = 290,
    TK_VIRTUALCATCHERCODE = 291,
    TK_TRAVERSECODE = 292,
    TK_CLEARCODE = 293,
    TK_GETBUFFERCODE = 294,
    TK_RELEASEBUFFERCODE = 295,
    TK_READBUFFERCODE = 296,
    TK_WRITEBUFFERCODE = 297,
    TK_SEGCOUNTCODE = 298,
    TK_CHARBUFFERCODE = 299,
    TK_PICKLECODE = 300,
    TK_VIRTUALCALLCODE = 301,
    TK_METHODCODE = 302,
    TK_INSTANCECODE = 303,
    TK_FROMTYPE = 304,
    TK_TOTYPE = 305,
    TK_TOSUBCLASS = 306,
    TK_INCLUDE = 307,
    TK_OPTINCLUDE = 308,
    TK_IMPORT = 309,
    TK_EXPHEADERCODE = 310,
    TK_MODHEADERCODE = 311,
    TK_TYPEHEADERCODE = 312,
    TK_MODULE = 313,
    TK_CMODULE = 314,
    TK_CONSMODULE = 315,
    TK_COMPOMODULE = 316,
    TK_CLASS = 317,
    TK_STRUCT = 318,
    TK_PUBLIC = 319,
    TK_PROTECTED = 320,
    TK_PRIVATE = 321,
    TK_SIGNALS = 322,
    TK_SIGNAL_METHOD = 323,
    TK_SLOTS = 324,
    TK_SLOT_METHOD = 325,
    TK_BOOL = 326,
    TK_SHORT = 327,
    TK_INT = 328,
    TK_LONG = 329,
    TK_FLOAT = 330,
    TK_DOUBLE = 331,
    TK_CHAR = 332,
    TK_WCHAR_T = 333,
    TK_VOID = 334,
    TK_PYOBJECT = 335,
    TK_PYTUPLE = 336,
    TK_PYLIST = 337,
    TK_PYDICT = 338,
    TK_PYCALLABLE = 339,
    TK_PYSLICE = 340,
    TK_PYTYPE = 341,
    TK_PYBUFFER = 342,
    TK_VIRTUAL = 343,
    TK_ENUM = 344,
    TK_SIGNED = 345,
    TK_UNSIGNED = 346,
    TK_SCOPE = 347,
    TK_LOGICAL_OR = 348,
    TK_CONST = 349,
    TK_STATIC = 350,
    TK_SIPSIGNAL = 351,
    TK_SIPSLOT = 352,
    TK_SIPANYSLOT = 353,
    TK_SIPRXCON = 354,
    TK_SIPRXDIS = 355,
    TK_SIPSLOTCON = 356,
    TK_SIPSLOTDIS = 357,
    TK_SIPSSIZET = 358,
    TK_NUMBER_VALUE = 359,
    TK_REAL_VALUE = 360,
    TK_TYPEDEF = 361,
    TK_NAMESPACE = 362,
    TK_TIMELINE = 363,
    TK_PLATFORMS = 364,
    TK_FEATURE = 365,
    TK_LICENSE = 366,
    TK_QCHAR_VALUE = 367,
    TK_TRUE_VALUE = 368,
    TK_FALSE_VALUE = 369,
    TK_NULL_VALUE = 370,
    TK_OPERATOR = 371,
    TK_THROW = 372,
    TK_QOBJECT = 373,
    TK_EXCEPTION = 374,
    TK_RAISECODE = 375,
    TK_VIRTERRORCODE = 376,
    TK_EXPLICIT = 377,
    TK_TEMPLATE = 378,
    TK_ELLIPSIS = 379,
    TK_DEFMETATYPE = 380,
    TK_DEFSUPERTYPE = 381,
    TK_PROPERTY = 382,
    TK_FORMAT = 383,
    TK_GET = 384,
    TK_ID = 385,
    TK_KWARGS = 386,
    TK_LANGUAGE = 387,
    TK_LICENSEE = 388,
    TK_NAME = 389,
    TK_OPTIONAL = 390,
    TK_ORDER = 391,
    TK_REMOVELEADING = 392,
    TK_SET = 393,
    TK_SIGNATURE = 394,
    TK_TIMESTAMP = 395,
    TK_TYPE = 396,
    TK_USEARGNAMES = 397,
    TK_ALLRAISEPYEXC = 398,
    TK_CALLSUPERINIT = 399,
    TK_DEFERRORHANDLER = 400,
    TK_VERSION = 401
  };
#endif
/* Tokens.  */
#define TK_API 258
#define TK_AUTOPYNAME 259
#define TK_DEFDOCSTRING 260
#define TK_DEFENCODING 261
#define TK_PLUGIN 262
#define TK_VIRTERRORHANDLER 263
#define TK_EXPTYPEHINTCODE 264
#define TK_TYPEHINTCODE 265
#define TK_DOCSTRING 266
#define TK_DOC 267
#define TK_EXPORTEDDOC 268
#define TK_EXTRACT 269
#define TK_MAKEFILE 270
#define TK_ACCESSCODE 271
#define TK_GETCODE 272
#define TK_SETCODE 273
#define TK_PREINITCODE 274
#define TK_INITCODE 275
#define TK_POSTINITCODE 276
#define TK_FINALCODE 277
#define TK_UNITCODE 278
#define TK_UNITPOSTINCLUDECODE 279
#define TK_MODCODE 280
#define TK_TYPECODE 281
#define TK_PREPYCODE 282
#define TK_COPYING 283
#define TK_MAPPEDTYPE 284
#define TK_CODELINE 285
#define TK_IF 286
#define TK_END 287
#define TK_NAME_VALUE 288
#define TK_PATH_VALUE 289
#define TK_STRING_VALUE 290
#define TK_VIRTUALCATCHERCODE 291
#define TK_TRAVERSECODE 292
#define TK_CLEARCODE 293
#define TK_GETBUFFERCODE 294
#define TK_RELEASEBUFFERCODE 295
#define TK_READBUFFERCODE 296
#define TK_WRITEBUFFERCODE 297
#define TK_SEGCOUNTCODE 298
#define TK_CHARBUFFERCODE 299
#define TK_PICKLECODE 300
#define TK_VIRTUALCALLCODE 301
#define TK_METHODCODE 302
#define TK_INSTANCECODE 303
#define TK_FROMTYPE 304
#define TK_TOTYPE 305
#define TK_TOSUBCLASS 306
#define TK_INCLUDE 307
#define TK_OPTINCLUDE 308
#define TK_IMPORT 309
#define TK_EXPHEADERCODE 310
#define TK_MODHEADERCODE 311
#define TK_TYPEHEADERCODE 312
#define TK_MODULE 313
#define TK_CMODULE 314
#define TK_CONSMODULE 315
#define TK_COMPOMODULE 316
#define TK_CLASS 317
#define TK_STRUCT 318
#define TK_PUBLIC 319
#define TK_PROTECTED 320
#define TK_PRIVATE 321
#define TK_SIGNALS 322
#define TK_SIGNAL_METHOD 323
#define TK_SLOTS 324
#define TK_SLOT_METHOD 325
#define TK_BOOL 326
#define TK_SHORT 327
#define TK_INT 328
#define TK_LONG 329
#define TK_FLOAT 330
#define TK_DOUBLE 331
#define TK_CHAR 332
#define TK_WCHAR_T 333
#define TK_VOID 334
#define TK_PYOBJECT 335
#define TK_PYTUPLE 336
#define TK_PYLIST 337
#define TK_PYDICT 338
#define TK_PYCALLABLE 339
#define TK_PYSLICE 340
#define TK_PYTYPE 341
#define TK_PYBUFFER 342
#define TK_VIRTUAL 343
#define TK_ENUM 344
#define TK_SIGNED 345
#define TK_UNSIGNED 346
#define TK_SCOPE 347
#define TK_LOGICAL_OR 348
#define TK_CONST 349
#define TK_STATIC 350
#define TK_SIPSIGNAL 351
#define TK_SIPSLOT 352
#define TK_SIPANYSLOT 353
#define TK_SIPRXCON 354
#define TK_SIPRXDIS 355
#define TK_SIPSLOTCON 356
#define TK_SIPSLOTDIS 357
#define TK_SIPSSIZET 358
#define TK_NUMBER_VALUE 359
#define TK_REAL_VALUE 360
#define TK_TYPEDEF 361
#define TK_NAMESPACE 362
#define TK_TIMELINE 363
#define TK_PLATFORMS 364
#define TK_FEATURE 365
#define TK_LICENSE 366
#define TK_QCHAR_VALUE 367
#define TK_TRUE_VALUE 368
#define TK_FALSE_VALUE 369
#define TK_NULL_VALUE 370
#define TK_OPERATOR 371
#define TK_THROW 372
#define TK_QOBJECT 373
#define TK_EXCEPTION 374
#define TK_RAISECODE 375
#define TK_VIRTERRORCODE 376
#define TK_EXPLICIT 377
#define TK_TEMPLATE 378
#define TK_ELLIPSIS 379
#define TK_DEFMETATYPE 380
#define TK_DEFSUPERTYPE 381
#define TK_PROPERTY 382
#define TK_FORMAT 383
#define TK_GET 384
#define TK_ID 385
#define TK_KWARGS 386
#define TK_LANGUAGE 387
#define TK_LICENSEE 388
#define TK_NAME 389
#define TK_OPTIONAL 390
#define TK_ORDER 391
#define TK_REMOVELEADING 392
#define TK_SET 393
#define TK_SIGNATURE 394
#define TK_TIMESTAMP 395
#define TK_TYPE 396
#define TK_USEARGNAMES 397
#define TK_ALLRAISEPYEXC 398
#define TK_CALLSUPERINIT 399
#define TK_DEFERRORHANDLER 400
#define TK_VERSION 401

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE YYSTYPE;
union YYSTYPE
{
#line 193 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:355  */

    char            qchar;
    char            *text;
    long            number;
    double          real;
    argDef          memArg;
    signatureDef    signature;
    signatureDef    *optsignature;
    throwArgs       *throwlist;
    codeBlock       *codeb;
    valueDef        value;
    valueDef        *valp;
    optFlags        optflags;
    optFlag         flag;
    scopedNameDef   *scpvalp;
    fcallDef        fcall;
    int             boolean;
    exceptionDef    exceptionbase;
    classDef        *klass;
    apiCfg          api;
    autoPyNameCfg   autopyname;
    compModuleCfg   compmodule;
    consModuleCfg   consmodule;
    defDocstringCfg defdocstring;
    defEncodingCfg  defencoding;
    defMetatypeCfg  defmetatype;
    defSupertypeCfg defsupertype;
    exceptionCfg    exception;
    docstringCfg    docstring;
    extractCfg      extract;
    featureCfg      feature;
    licenseCfg      license;
    importCfg       import;
    includeCfg      include;
    moduleCfg       module;
    pluginCfg       plugin;
    propertyCfg     property;
    variableCfg     variable;
    vehCfg          veh;
    int             token;

#line 614 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:355  */
};
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_HOME_BOB_HG_SIP_SIP_4_18_SNAPSHOT_A4F8A7810CC3_SIPGEN_PARSER_H_INCLUDED  */

/* Copy the second part of user declarations.  */

#line 629 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:358  */

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

#ifndef YY_ATTRIBUTE
# if (defined __GNUC__                                               \
      && (2 < __GNUC__ || (__GNUC__ == 2 && 96 <= __GNUC_MINOR__)))  \
     || defined __SUNPRO_C && 0x5110 <= __SUNPRO_C
#  define YY_ATTRIBUTE(Spec) __attribute__(Spec)
# else
#  define YY_ATTRIBUTE(Spec) /* empty */
# endif
#endif

#ifndef YY_ATTRIBUTE_PURE
# define YY_ATTRIBUTE_PURE   YY_ATTRIBUTE ((__pure__))
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# define YY_ATTRIBUTE_UNUSED YY_ATTRIBUTE ((__unused__))
#endif

#if !defined _Noreturn \
     && (!defined __STDC_VERSION__ || __STDC_VERSION__ < 201112)
# if defined _MSC_VER && 1200 <= _MSC_VER
#  define _Noreturn __declspec (noreturn)
# else
#  define _Noreturn YY_ATTRIBUTE ((__noreturn__))
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

#if defined __GNUC__ && 407 <= __GNUC__ * 100 + __GNUC_MINOR__
/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN \
    _Pragma ("GCC diagnostic push") \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")\
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# define YY_IGNORE_MAYBE_UNINITIALIZED_END \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif


#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYSIZE_T yynewbytes;                                            \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / sizeof (*yyptr);                          \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, (Count) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYSIZE_T yyi;                         \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  4
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   1536

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  169
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  241
/* YYNRULES -- Number of rules.  */
#define YYNRULES  566
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  988

/* YYTRANSLATE[YYX] -- Symbol number corresponding to YYX as returned
   by yylex, with out-of-bounds checking.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   401

#define YYTRANSLATE(YYX)                                                \
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, without out-of-bounds checking.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   154,     2,     2,     2,   167,   159,     2,
     147,   148,   157,   156,   149,   155,     2,   158,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,   164,   153,
     162,   150,   163,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   165,     2,   166,   168,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   151,   160,   152,   161,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      75,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    87,    88,    89,    90,    91,    92,    93,    94,
      95,    96,    97,    98,    99,   100,   101,   102,   103,   104,
     105,   106,   107,   108,   109,   110,   111,   112,   113,   114,
     115,   116,   117,   118,   119,   120,   121,   122,   123,   124,
     125,   126,   127,   128,   129,   130,   131,   132,   133,   134,
     135,   136,   137,   138,   139,   140,   141,   142,   143,   144,
     145,   146
};

#if YYDEBUG
  /* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,   546,   546,   547,   550,   550,   569,   570,   571,   572,
     573,   574,   575,   576,   577,   578,   579,   580,   581,   582,
     583,   584,   585,   586,   587,   588,   589,   590,   591,   592,
     593,   594,   595,   596,   597,   598,   599,   600,   601,   602,
     603,   604,   607,   608,   609,   610,   611,   612,   613,   614,
     615,   616,   617,   618,   631,   637,   642,   647,   648,   658,
     665,   674,   679,   684,   685,   695,   702,   710,   715,   720,
     721,   731,   738,   767,   772,   777,   778,   788,   795,   821,
     829,   834,   835,   846,   852,   860,   910,   914,  1021,  1026,
    1027,  1038,  1041,  1044,  1058,  1074,  1079,  1079,  1102,  1102,
    1167,  1181,  1182,  1185,  1186,  1187,  1191,  1195,  1204,  1213,
    1222,  1223,  1226,  1240,  1240,  1277,  1278,  1281,  1282,  1285,
    1285,  1314,  1315,  1318,  1324,  1330,  1335,  1340,  1341,  1351,
    1358,  1358,  1384,  1385,  1388,  1394,  1407,  1410,  1413,  1416,
    1421,  1422,  1427,  1433,  1470,  1478,  1484,  1489,  1490,  1503,
    1511,  1519,  1527,  1537,  1548,  1553,  1558,  1559,  1569,  1576,
    1587,  1592,  1597,  1598,  1608,  1615,  1635,  1640,  1645,  1646,
    1656,  1663,  1667,  1672,  1673,  1683,  1686,  1689,  1703,  1721,
    1726,  1731,  1732,  1742,  1749,  1753,  1758,  1759,  1769,  1772,
    1775,  1789,  1800,  1810,  1810,  1823,  1828,  1829,  1846,  1858,
    1876,  1888,  1900,  1912,  1924,  1936,  1953,  1957,  1962,  1963,
    1973,  1976,  1979,  1982,  1996,  1997,  2013,  2016,  2019,  2028,
    2034,  2039,  2040,  2051,  2057,  2065,  2073,  2079,  2084,  2089,
    2090,  2100,  2107,  2110,  2115,  2118,  2123,  2126,  2131,  2137,
    2143,  2149,  2154,  2159,  2164,  2169,  2174,  2179,  2184,  2189,
    2194,  2199,  2204,  2209,  2215,  2220,  2226,  2232,  2238,  2244,
    2250,  2255,  2261,  2267,  2272,  2278,  2284,  2290,  2295,  2296,
    2306,  2313,  2393,  2396,  2401,  2406,  2407,  2417,  2424,  2427,
    2430,  2439,  2445,  2450,  2451,  2462,  2468,  2479,  2484,  2487,
    2488,  2498,  2498,  2519,  2522,  2527,  2530,  2535,  2536,  2539,
    2540,  2543,  2544,  2545,  2583,  2584,  2587,  2588,  2591,  2594,
    2599,  2600,  2618,  2621,  2624,  2627,  2630,  2633,  2638,  2641,
    2644,  2647,  2650,  2653,  2656,  2661,  2676,  2679,  2684,  2685,
    2693,  2698,  2701,  2706,  2715,  2725,  2729,  2733,  2737,  2741,
    2745,  2751,  2756,  2762,  2780,  2802,  2841,  2847,  2841,  2890,
    2890,  2916,  2921,  2927,  2921,  2966,  2967,  2970,  2971,  2974,
    3018,  3021,  3024,  3027,  3032,  3035,  3040,  3041,  3044,  3045,
    3046,  3047,  3048,  3049,  3050,  3051,  3052,  3053,  3057,  3061,
    3065,  3076,  3087,  3098,  3109,  3120,  3131,  3142,  3153,  3164,
    3175,  3186,  3197,  3198,  3199,  3200,  3211,  3222,  3233,  3240,
    3247,  3254,  3263,  3276,  3281,  3282,  3294,  3301,  3308,  3317,
    3321,  3326,  3327,  3337,  3340,  3343,  3357,  3358,  3361,  3364,
    3369,  3431,  3431,  3432,  3435,  3481,  3484,  3484,  3495,  3498,
    3498,  3510,  3513,  3518,  3536,  3556,  3592,  3673,  3674,  3675,
    3676,  3677,  3678,  3679,  3680,  3681,  3682,  3683,  3684,  3685,
    3686,  3687,  3688,  3689,  3690,  3691,  3692,  3693,  3694,  3695,
    3696,  3697,  3698,  3699,  3700,  3701,  3704,  3707,  3712,  3715,
    3723,  3726,  3732,  3736,  3748,  3752,  3758,  3762,  3785,  3789,
    3795,  3798,  3803,  3806,  3811,  3814,  3819,  3871,  3876,  3882,
    3905,  3917,  3929,  3941,  3960,  3971,  3988,  4005,  4014,  4021,
    4021,  4022,  4022,  4023,  4027,  4027,  4028,  4032,  4033,  4037,
    4037,  4038,  4041,  4096,  4102,  4107,  4108,  4120,  4123,  4126,
    4141,  4156,  4173,  4178,  4192,  4295,  4298,  4306,  4309,  4312,
    4317,  4325,  4336,  4351,  4355,  4359,  4363,  4367,  4371,  4375,
    4379,  4383,  4387,  4391,  4395,  4399,  4403,  4407,  4411,  4415,
    4419,  4423,  4427,  4431,  4435,  4439,  4443,  4447,  4451,  4455,
    4461,  4467,  4483,  4486,  4494,  4500,  4507
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 0
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "TK_API", "TK_AUTOPYNAME",
  "TK_DEFDOCSTRING", "TK_DEFENCODING", "TK_PLUGIN", "TK_VIRTERRORHANDLER",
  "TK_EXPTYPEHINTCODE", "TK_TYPEHINTCODE", "TK_DOCSTRING", "TK_DOC",
  "TK_EXPORTEDDOC", "TK_EXTRACT", "TK_MAKEFILE", "TK_ACCESSCODE",
  "TK_GETCODE", "TK_SETCODE", "TK_PREINITCODE", "TK_INITCODE",
  "TK_POSTINITCODE", "TK_FINALCODE", "TK_UNITCODE",
  "TK_UNITPOSTINCLUDECODE", "TK_MODCODE", "TK_TYPECODE", "TK_PREPYCODE",
  "TK_COPYING", "TK_MAPPEDTYPE", "TK_CODELINE", "TK_IF", "TK_END",
  "TK_NAME_VALUE", "TK_PATH_VALUE", "TK_STRING_VALUE",
  "TK_VIRTUALCATCHERCODE", "TK_TRAVERSECODE", "TK_CLEARCODE",
  "TK_GETBUFFERCODE", "TK_RELEASEBUFFERCODE", "TK_READBUFFERCODE",
  "TK_WRITEBUFFERCODE", "TK_SEGCOUNTCODE", "TK_CHARBUFFERCODE",
  "TK_PICKLECODE", "TK_VIRTUALCALLCODE", "TK_METHODCODE",
  "TK_INSTANCECODE", "TK_FROMTYPE", "TK_TOTYPE", "TK_TOSUBCLASS",
  "TK_INCLUDE", "TK_OPTINCLUDE", "TK_IMPORT", "TK_EXPHEADERCODE",
  "TK_MODHEADERCODE", "TK_TYPEHEADERCODE", "TK_MODULE", "TK_CMODULE",
  "TK_CONSMODULE", "TK_COMPOMODULE", "TK_CLASS", "TK_STRUCT", "TK_PUBLIC",
  "TK_PROTECTED", "TK_PRIVATE", "TK_SIGNALS", "TK_SIGNAL_METHOD",
  "TK_SLOTS", "TK_SLOT_METHOD", "TK_BOOL", "TK_SHORT", "TK_INT", "TK_LONG",
  "TK_FLOAT", "TK_DOUBLE", "TK_CHAR", "TK_WCHAR_T", "TK_VOID",
  "TK_PYOBJECT", "TK_PYTUPLE", "TK_PYLIST", "TK_PYDICT", "TK_PYCALLABLE",
  "TK_PYSLICE", "TK_PYTYPE", "TK_PYBUFFER", "TK_VIRTUAL", "TK_ENUM",
  "TK_SIGNED", "TK_UNSIGNED", "TK_SCOPE", "TK_LOGICAL_OR", "TK_CONST",
  "TK_STATIC", "TK_SIPSIGNAL", "TK_SIPSLOT", "TK_SIPANYSLOT",
  "TK_SIPRXCON", "TK_SIPRXDIS", "TK_SIPSLOTCON", "TK_SIPSLOTDIS",
  "TK_SIPSSIZET", "TK_NUMBER_VALUE", "TK_REAL_VALUE", "TK_TYPEDEF",
  "TK_NAMESPACE", "TK_TIMELINE", "TK_PLATFORMS", "TK_FEATURE",
  "TK_LICENSE", "TK_QCHAR_VALUE", "TK_TRUE_VALUE", "TK_FALSE_VALUE",
  "TK_NULL_VALUE", "TK_OPERATOR", "TK_THROW", "TK_QOBJECT", "TK_EXCEPTION",
  "TK_RAISECODE", "TK_VIRTERRORCODE", "TK_EXPLICIT", "TK_TEMPLATE",
  "TK_ELLIPSIS", "TK_DEFMETATYPE", "TK_DEFSUPERTYPE", "TK_PROPERTY",
  "TK_FORMAT", "TK_GET", "TK_ID", "TK_KWARGS", "TK_LANGUAGE",
  "TK_LICENSEE", "TK_NAME", "TK_OPTIONAL", "TK_ORDER", "TK_REMOVELEADING",
  "TK_SET", "TK_SIGNATURE", "TK_TIMESTAMP", "TK_TYPE", "TK_USEARGNAMES",
  "TK_ALLRAISEPYEXC", "TK_CALLSUPERINIT", "TK_DEFERRORHANDLER",
  "TK_VERSION", "'('", "')'", "','", "'='", "'{'", "'}'", "';'", "'!'",
  "'-'", "'+'", "'*'", "'/'", "'&'", "'|'", "'~'", "'<'", "'>'", "':'",
  "'['", "']'", "'%'", "'^'", "$accept", "specification", "statement",
  "$@1", "modstatement", "nsstatement", "defdocstring",
  "defdocstring_args", "defdocstring_arg_list", "defdocstring_arg",
  "defencoding", "defencoding_args", "defencoding_arg_list",
  "defencoding_arg", "plugin", "plugin_args", "plugin_arg_list",
  "plugin_arg", "virterrorhandler", "veh_args", "veh_arg_list", "veh_arg",
  "api", "api_args", "api_arg_list", "api_arg", "exception",
  "baseexception", "exception_body", "exception_body_directives",
  "exception_body_directive", "raisecode", "mappedtype", "$@2",
  "mappedtypetmpl", "$@3", "mtdefinition", "mtbody", "mtline",
  "mtfunction", "namespace", "$@4", "optnsbody", "nsbody", "platforms",
  "$@5", "platformlist", "platform", "feature", "feature_args",
  "feature_arg_list", "feature_arg", "timeline", "$@6", "qualifierlist",
  "qualifiername", "ifstart", "oredqualifiers", "qualifiers", "ifend",
  "license", "license_args", "license_arg_list", "license_arg",
  "defmetatype", "defmetatype_args", "defmetatype_arg_list",
  "defmetatype_arg", "defsupertype", "defsupertype_args",
  "defsupertype_arg_list", "defsupertype_arg", "consmodule",
  "consmodule_args", "consmodule_arg_list", "consmodule_arg",
  "consmodule_body", "consmodule_body_directives",
  "consmodule_body_directive", "compmodule", "compmodule_args",
  "compmodule_arg_list", "compmodule_arg", "compmodule_body",
  "compmodule_body_directives", "compmodule_body_directive", "module",
  "module_args", "$@7", "module_arg_list", "module_arg", "module_body",
  "module_body_directives", "module_body_directive", "dottedname",
  "optnumber", "include", "include_args", "include_arg_list",
  "include_arg", "optinclude", "import", "import_args", "import_arg_list",
  "import_arg", "optaccesscode", "optgetcode", "optsetcode", "copying",
  "exphdrcode", "modhdrcode", "typehdrcode", "travcode", "clearcode",
  "getbufcode", "releasebufcode", "readbufcode", "writebufcode",
  "segcountcode", "charbufcode", "instancecode", "picklecode", "finalcode",
  "modcode", "typecode", "preinitcode", "initcode", "postinitcode",
  "unitcode", "unitpostinccode", "prepycode", "exptypehintcode",
  "modtypehintcode", "classtypehintcode", "doc", "exporteddoc",
  "autopyname", "autopyname_args", "autopyname_arg_list", "autopyname_arg",
  "docstring", "docstring_args", "docstring_arg_list", "docstring_arg",
  "optdocstring", "extract", "extract_args", "extract_arg_list",
  "extract_arg", "makefile", "codeblock", "codelines", "enum", "$@8",
  "optfilename", "optname", "optenumbody", "enumbody", "enumline",
  "optcomma", "optenumassign", "optassign", "expr", "binop", "optunop",
  "value", "optcast", "scopedname", "scopepart", "bool_value",
  "simplevalue", "exprlist", "typedef", "struct", "$@9", "$@10",
  "classtmpl", "$@11", "template", "class", "$@12", "$@13", "superclasses",
  "superlist", "superclass", "class_access", "optclassbody", "classbody",
  "classline", "property", "property_args", "property_arg_list",
  "property_arg", "property_body", "property_body_directives",
  "property_body_directive", "name_or_string", "optslot", "dtor", "ctor",
  "$@14", "simplector", "optctorsig", "$@15", "optsig", "$@16",
  "optvirtual", "function", "operatorname", "optconst", "optabstract",
  "optflags", "flaglist", "flag", "flagvalue", "virtualcallcode",
  "methodcode", "virtualcatchercode", "arglist", "rawarglist", "argvalue",
  "varmember", "$@17", "$@18", "simple_varmem", "$@19", "varmem", "member",
  "$@20", "variable", "variable_body", "variable_body_directives",
  "variable_body_directive", "cpptype", "argtype", "optref", "deref",
  "basetype", "cpptypelist", "optexceptions", "exceptionlist", YY_NULLPTR
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[NUM] -- (External) token number corresponding to the
   (internal) symbol number NUM (which must be that of a token).  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,   302,   303,   304,
     305,   306,   307,   308,   309,   310,   311,   312,   313,   314,
     315,   316,   317,   318,   319,   320,   321,   322,   323,   324,
     325,   326,   327,   328,   329,   330,   331,   332,   333,   334,
     335,   336,   337,   338,   339,   340,   341,   342,   343,   344,
     345,   346,   347,   348,   349,   350,   351,   352,   353,   354,
     355,   356,   357,   358,   359,   360,   361,   362,   363,   364,
     365,   366,   367,   368,   369,   370,   371,   372,   373,   374,
     375,   376,   377,   378,   379,   380,   381,   382,   383,   384,
     385,   386,   387,   388,   389,   390,   391,   392,   393,   394,
     395,   396,   397,   398,   399,   400,   401,    40,    41,    44,
      61,   123,   125,    59,    33,    45,    43,    42,    47,    38,
     124,   126,    60,    62,    58,    91,    93,    37,    94
};
# endif

#define YYPACT_NINF -722

#define yypact_value_is_default(Yystate) \
  (!!((Yystate) == (-722)))

#define YYTABLE_NINF -533

#define yytable_value_is_error(Yytable_value) \
  0

  /* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
     STATE-NUM.  */
static const yytype_int16 yypact[] =
{
    -722,   145,  -722,   925,  -722,  -722,    31,    62,    84,    37,
      67,   133,   133,   133,   133,    76,   171,   133,   133,   133,
     133,   133,   133,   133,   133,  1412,   127,  -722,  -722,     9,
     231,    50,   133,   133,   133,    53,   162,    55,    61,   245,
     245,  -722,  -722,  -722,   208,  -722,  -722,  -722,  -722,  -722,
    -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,   269,   235,
     338,  1412,  -722,  1377,   285,  -722,  -722,    77,    85,  1377,
     245,   182,  -722,    65,    69,  -722,  -722,  -722,  -722,  -722,
    -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,
    -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,
    -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,
    -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,   -25,  -722,
    -722,  -722,  -722,   329,  -722,  -722,  -722,    35,  -722,   217,
     118,  -722,  -722,   241,  -722,  -722,   302,  -722,  -722,   310,
    -722,  -722,   328,   133,  -722,  -722,   279,  -722,  -722,  -722,
    -722,   136,   133,   313,  -722,  -722,  -722,  -722,  -722,  -722,
    -722,  -722,   245,   215,    28,  -722,   164,  -722,  -722,  -722,
     336,  -722,  -722,  -722,  -722,  -722,  -722,   240,   275,  -722,
     326,   342,   277,  -722,   345,   350,  -722,   366,    26,  -722,
    -722,   215,  -722,  -722,  -722,   422,  -722,  -722,    81,  -722,
     351,   352,  -722,   370,  -722,  -722,   213,   215,   358,    74,
    1377,   372,  -722,  -722,   374,  -722,  -722,   245,  1377,  1412,
     447,    83,   330,   -42,  -722,   360,   362,   192,  -722,   363,
     202,  -722,   364,   253,  -722,   365,   259,  -722,   367,   265,
    -722,  -722,  -722,  -722,   368,   369,   271,  -722,  -722,  -722,
     133,   366,   483,  -722,   375,   487,   429,   377,   376,   382,
     383,   274,  -722,   384,   284,  -722,   385,   386,   387,   388,
     389,   390,   391,   393,   286,  -722,   211,  -722,   326,  -722,
    -722,   394,   290,  -722,   229,  -722,   395,   292,  -722,   229,
    -722,   396,   396,  -722,  -722,   -42,   215,   392,   397,   494,
     513,   400,   294,  -722,   401,   402,   404,   405,   298,  -722,
    -722,   818,   245,   215,  -722,   -33,   408,   301,  -722,   409,
     303,  -722,  -722,   -11,   215,  -722,   818,   410,   399,   100,
     412,   413,   414,   415,   416,   417,   419,  -722,    27,    -2,
     406,   423,   425,   430,   484,  -722,  -722,   335,   475,  -722,
     118,   545,  -722,   241,   549,  -722,   302,   552,  -722,   310,
     553,  -722,   328,   554,   485,  -722,   136,  -722,   440,   105,
    -722,   441,  -722,    32,  -722,   269,   557,   340,  -722,   164,
     559,  -722,   336,   560,   561,   162,   340,   340,   340,   564,
     490,  -722,   240,   451,    92,  -722,  -722,    42,  -722,  -722,
    -722,  -722,   162,  -722,   342,  -722,  -722,    40,  -722,  -722,
     162,  -722,   345,  -722,  -722,    47,  -722,  -722,   296,   215,
     215,   452,  -722,   453,   571,  1155,   454,  -722,    15,  -722,
    -722,    29,  -722,   335,  -722,   370,   570,   573,   574,   575,
    -722,   213,   269,   269,   269,   269,   269,   464,   465,   269,
     466,   467,  -722,   269,   463,    -7,   468,  1377,  -722,   162,
    -722,   372,   162,  -722,   374,  -722,  -722,   469,   239,   470,
    -722,  1377,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,
    -722,   471,  -722,   472,  -722,  -722,  -722,   818,  -722,  -722,
    -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,
    -722,  -722,  -722,  -722,  -722,   140,   483,  -722,   227,  -722,
    -722,   585,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,
    -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,   488,
    -722,  -722,   492,   133,   473,  -722,  -722,  -722,   474,  -722,
    -722,  -722,   476,  -722,  -722,  -722,  -722,   479,  -722,   245,
    -722,  -722,   347,  -722,   482,  -722,   990,  -722,  -722,  -722,
    -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,
     215,   215,   215,   215,   215,   818,   818,   215,   530,   818,
     215,   486,  -722,  -722,    97,  -722,  -722,  -722,  -722,  -722,
    -722,   441,   530,   133,   133,   133,  -722,  -722,    59,  -722,
     615,   491,  -722,  -722,   496,   478,  -722,  -722,  -722,  -722,
    -722,   133,   133,   133,   133,  1377,    75,  -722,  -722,  -722,
    -722,  -722,  -722,  -722,  -722,  -722,   495,   307,  -722,   498,
     312,  -722,  -722,  -722,  -722,  -722,   296,   366,   481,   481,
     499,  -722,  -722,   500,   347,  -722,   489,  -722,  -722,   463,
     463,   463,  -722,  -722,   502,   503,  -722,  -722,   517,  -722,
    -722,   245,   232,  -722,   135,   133,    51,  -722,  -722,  -722,
    -722,  -722,  -722,   517,  -722,  -722,  -722,  -722,  -722,   133,
     623,   493,   530,   326,  -722,  -722,  -722,  -722,   622,   504,
    -722,   621,  -722,   488,   624,  -722,   492,  -722,  1089,   507,
     508,   486,   215,   510,  -722,  1377,  -722,  -722,  -722,   269,
     269,   518,   514,    43,  -722,  -722,  -722,  -722,  -722,  -722,
     486,  -722,  -722,  -722,  -722,  -722,  -722,   252,  -722,   516,
    -722,   514,  -722,   133,   648,  -722,   517,   519,   524,  -722,
    -722,  -722,  -722,  -722,   133,   133,   525,   133,   133,   133,
     133,   133,   133,   133,   133,   133,   133,   133,   133,   604,
     604,   604,   511,  -722,  -722,   515,  -722,  -722,   531,  -722,
    -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,
    -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,
    -722,  -722,   758,  -722,  -722,  -722,  -722,  -722,   521,  -722,
    -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,   528,  -722,
     316,   215,   215,   245,   576,   215,  -722,  -722,  -722,  -722,
    -722,  -722,  -722,    57,  -722,  -722,   532,  -722,   215,  -722,
     133,  -722,   514,   326,   818,  -722,  -722,   818,  -722,  -722,
    -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,
    -722,   520,   522,   523,  -722,  1210,  1210,  1322,  1266,   650,
     159,   537,  -722,  -722,   656,  -722,  -722,   215,  -722,  -722,
     366,   318,  -722,   526,   246,   526,  -722,   215,  -722,   542,
     544,  -722,  -722,  -722,  -722,  -722,  -722,  -722,    71,  -722,
     525,  -722,   546,   547,   550,   320,  -722,   229,  -722,   548,
     541,  -722,   245,  -722,   551,   232,   324,   555,   526,   530,
     517,   562,   666,   335,   669,  -722,   159,  -722,  -722,  -722,
      49,  -722,   563,  -722,   366,  1377,   660,  -722,   486,   699,
     565,   517,   215,  -722,  -722,  -722,  -722,   566,  -722,   517,
     567,   133,   676,   232,  -722,   660,   660,   215,   558,  -722,
     514,   818,  -722,   133,   667,   676,   676,   526,  -722,   569,
     215,   568,  -722,   133,  -722,   667,   667,   572,   577,   699,
     578,   581,  -722,  -722,  -722,   699,   818,   660,   660,  -722,
     660,   579,  -722,   676,  -722,   582,  -722,  -722
};

  /* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
     Performed when YYTABLE does not specify something else to do.  Zero
     means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       4,     4,     2,     0,     1,     3,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   142,   330,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   544,   534,   537,   538,   542,   543,   547,   548,   549,
     550,   551,   552,   553,   554,   555,   556,   557,   295,     0,
     535,     0,   558,     0,     0,   130,   119,     0,   144,     0,
       0,     0,   559,     0,     0,     5,    41,    19,    20,     9,
      40,    14,    48,    38,    39,    44,    16,    17,    15,    42,
      43,    18,    21,    22,     7,     8,     6,    11,    12,    13,
      10,    23,    24,    53,    25,    26,    27,    28,    29,    30,
      31,    32,    33,    34,    35,    36,    37,    50,   530,   328,
      49,    45,    47,   349,    46,    51,    52,     0,   527,     0,
       0,    78,    55,     0,    54,    61,     0,    60,    67,     0,
      66,    73,     0,     0,   289,   261,     0,   262,   264,   265,
     281,     0,     0,   293,   255,   256,   257,   258,   259,   253,
     260,   238,     0,   470,   295,   219,     0,   218,   225,   227,
       0,   226,   239,   240,   241,   214,   215,     0,   206,   193,
     216,     0,   171,   166,     0,   184,   179,   352,   346,   540,
     296,   470,   545,   533,   536,   539,   546,   527,     0,   113,
       0,     0,   125,     0,   124,   145,     0,   470,     0,    86,
       0,     0,   153,   154,     0,   159,   160,     0,     0,     0,
       0,   470,     0,   525,    79,     0,     0,     0,    81,     0,
       0,    57,     0,     0,    63,     0,     0,    69,     0,     0,
      75,    72,   290,   288,     0,     0,     0,   283,   280,   294,
       0,   532,     0,    96,   136,     0,   140,     0,     0,     0,
       0,     0,   221,     0,     0,   229,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   196,     0,   191,   216,   217,
     192,     0,     0,   168,     0,   165,     0,     0,   181,     0,
     178,   355,   355,   291,   541,   525,   470,     0,   115,     0,
       0,     0,     0,   127,     0,     0,     0,     0,     0,   147,
     143,   487,     0,   470,   560,     0,     0,     0,   156,     0,
       0,   162,   329,     0,   470,   350,   487,   513,     0,     0,
       0,   438,   437,   439,   440,   442,   443,   457,   460,   464,
       0,   441,   444,     0,   529,   526,   523,     0,     0,    80,
       0,     0,    56,     0,     0,    62,     0,     0,    68,     0,
       0,    74,     0,     0,     0,   282,     0,   287,   474,     0,
     472,     0,   137,     0,   135,   295,     0,     0,   220,     0,
       0,   228,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   195,     0,     0,   272,   210,   211,     0,   208,   212,
     213,   194,     0,   167,     0,   175,   176,     0,   173,   177,
       0,   180,     0,   188,   189,     0,   186,   190,   360,   470,
     470,     0,   522,     0,     0,     0,     0,   134,     0,   132,
     123,     0,   121,     0,   126,     0,     0,     0,     0,     0,
     146,     0,   295,   295,   295,   295,   295,     0,     0,   295,
       0,   486,   488,   295,   308,     0,     0,     0,   351,     0,
     155,     0,     0,   161,     0,   531,    98,     0,     0,     0,
     458,     0,   462,   463,   448,   447,   449,   450,   452,   453,
     461,   445,   465,   446,   459,   451,   454,   487,   528,   416,
     417,    83,    84,    82,    59,    58,    65,    64,    71,    70,
      77,    76,   285,   286,   284,     0,     0,   471,     0,    97,
     138,     0,   141,   223,   331,   332,   224,   222,   231,   230,
     198,   199,   200,   201,   202,   203,   204,   205,   197,     0,
     266,   273,     0,     0,     0,   209,   170,   169,     0,   174,
     183,   182,     0,   187,   361,   362,   363,   356,   357,     0,
     353,   347,   297,   344,     0,   117,     0,   349,   114,   131,
     133,   120,   122,   129,   128,   150,   151,   152,   149,   148,
     470,   470,   470,   470,   470,   487,   487,   470,   466,     0,
     470,   326,   498,    87,     0,    85,   561,   158,   157,   164,
     163,     0,   466,     0,     0,     0,   517,   518,     0,   515,
     232,     0,   455,   456,     0,   214,   478,   479,   476,   475,
     473,     0,     0,     0,     0,     0,     0,   101,   111,   103,
     104,   105,   109,   106,   110,   139,     0,     0,   268,     0,
       0,   275,   271,   207,   172,   185,   360,   359,   364,   364,
     306,   301,   302,     0,   298,   299,     0,   116,   118,   308,
     308,   308,   493,   494,     0,     0,   497,   467,   562,   489,
     524,     0,   309,   310,   318,     0,     0,    89,    93,    91,
      92,    94,    99,   562,   519,   520,   521,   514,   516,     0,
     234,     0,   466,   216,   254,   250,   107,   108,     0,     0,
     102,     0,   267,     0,     0,   274,     0,   358,   431,     0,
       0,   326,   470,     0,   300,     0,   490,   491,   492,   295,
     295,     0,   468,     0,   312,   313,   314,   315,   316,   317,
     326,   319,   321,   322,   323,   324,   320,     0,    95,     0,
      90,   468,   233,     0,   236,   434,   562,     0,     0,   100,
     270,   269,   277,   276,     0,     0,   330,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   418,
     418,   418,     0,   499,   501,   509,   504,   421,     0,   373,
     370,   368,   369,   379,   380,   381,   382,   383,   384,   385,
     386,   387,   388,   389,   390,   378,   391,   377,   375,   374,
     371,   372,   431,   366,   376,   393,   392,   423,     0,   511,
     394,   503,   506,   507,   508,   354,   348,   307,   304,   292,
       0,   470,   470,   564,     0,   470,   327,   311,   339,   336,
     335,   340,   338,   333,   337,   325,     0,    88,   470,   235,
       0,   512,   468,   216,   487,   263,   252,   487,   242,   243,
     244,   245,   246,   247,   248,   249,   251,   397,   396,   395,
     419,     0,     0,     0,   401,     0,     0,     0,     0,     0,
       0,   409,   365,   367,     0,   305,   303,   470,   495,   496,
     565,     0,   469,   428,   326,   428,   237,   470,   477,     0,
       0,   398,   399,   400,   509,   500,   502,   510,     0,   505,
       0,   422,     0,     0,     0,     0,   404,     0,   402,     0,
       0,   563,     0,   429,     0,   342,     0,     0,   428,   466,
     562,     0,     0,     0,     0,   403,     0,   413,   414,   415,
       0,   411,     0,   345,   566,     0,   482,   334,   326,   278,
       0,   562,   470,   406,   407,   408,   405,     0,   412,   562,
       0,     0,   484,   343,   279,   482,   482,   470,   425,   410,
     468,   487,   483,     0,   480,   484,   484,   428,   426,     0,
     470,     0,   485,     0,   436,   480,   480,     0,     0,   278,
       0,     0,   481,   433,   435,   278,   487,   482,   482,   430,
     482,     0,   424,   484,   112,     0,   420,   427
};

  /* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -722,  -722,   714,  -722,  -722,  -387,  -722,  -722,  -722,   373,
    -722,  -722,  -722,   361,  -722,  -722,  -722,   371,  -722,  -722,
    -722,   398,  -722,  -722,  -722,   378,  -646,  -722,  -722,  -722,
      54,  -722,  -722,  -722,  -722,  -722,   138,  -722,   134,  -722,
    -632,  -722,  -722,  -722,  -722,  -722,  -722,   321,  -722,  -722,
    -722,   299,  -722,  -722,  -722,   323,  -239,  -722,  -722,  -235,
    -722,  -722,  -722,   308,  -722,  -722,  -722,   293,  -722,  -722,
    -722,   289,  -722,  -722,  -722,   353,  -722,  -722,   348,  -722,
    -722,  -722,   344,  -722,  -722,   346,  -722,  -722,  -722,  -722,
     379,  -722,  -722,   380,    19,  -259,  -722,  -722,  -722,   403,
    -722,  -722,  -722,  -722,   381,  -722,  -722,  -722,  -722,  -722,
    -722,  -473,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,
    -602,  -722,  -722,  -722,  -586,  -722,  -722,  -722,  -722,  -722,
    -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,  -722,    66,
    -250,  -722,  -722,    68,  -674,  -722,  -722,  -722,   427,  -722,
     -12,  -722,  -472,  -722,  -722,  -139,  -722,  -722,   121,  -722,
    -722,  -233,  -715,  -722,  -722,  -567,  -722,   -26,   587,  -358,
    -722,  -722,  -585,  -572,  -722,  -722,  -722,  -722,   759,  -204,
    -722,  -722,   480,  -722,   130,  -722,   128,  -722,   -22,  -722,
    -722,  -722,  -142,  -722,  -722,  -145,  -406,  -286,  -722,  -722,
    -722,   -83,  -722,  -722,  -720,  -722,  -722,    12,  -722,  -561,
    -699,  -174,  -722,   272,  -722,  -483,  -697,  -721,  -308,  -722,
     200,  -722,  -722,  -722,  -356,  -722,   -77,  -722,  -722,    20,
    -722,  -722,   185,     0,  -722,   580,   588,   -21,  -194,  -631,
    -722
};

  /* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     1,     2,     3,    75,    76,    77,   134,   230,   231,
      78,   137,   233,   234,    79,   140,   236,   237,    80,   143,
     239,   240,    81,   131,   227,   228,    82,   313,   585,   666,
     667,   668,    83,   371,    84,   591,   509,   616,   617,   618,
      85,   298,   426,   556,    86,   201,   431,   432,    87,   204,
     302,   303,    88,   200,   428,   429,    89,   256,   257,    90,
      91,   207,   308,   309,    92,   212,   317,   318,    93,   215,
     320,   321,    94,   182,   282,   283,   285,   407,   408,    95,
     185,   287,   288,   290,   415,   416,    96,   178,   278,   274,
     275,   277,   397,   398,   179,   280,    97,   167,   261,   262,
      98,    99,   171,   264,   265,   680,   734,   831,   100,   101,
     102,   103,   774,   775,   776,   777,   778,   779,   780,   781,
     622,   783,   784,   104,   623,   105,   106,   107,   108,   109,
     110,   111,   112,   786,   113,   114,   399,   530,   627,   628,
     944,   533,   630,   631,   945,   115,   152,   246,   247,   116,
     145,   146,   117,   421,   250,   191,   643,   644,   645,   866,
     702,   582,   662,   720,   727,   663,   664,   118,   119,   516,
     825,   906,   120,   121,   292,   639,   122,   220,   557,   124,
     291,   638,   419,   547,   548,   549,   699,   792,   793,   794,
     861,   895,   896,   898,   920,   921,   491,   851,   795,   796,
     859,   797,   959,   968,   904,   925,   798,   799,   343,   658,
     815,   253,   369,   370,   609,   964,   942,   954,   450,   451,
     452,   800,   855,   856,   801,   858,   802,   803,   857,   804,
     469,   598,   599,   453,   454,   346,   223,   128,   315,   712,
     871
};

  /* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
     positive, shift that token.  If negative, reduce the rule whose
     number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
     147,   148,   149,   127,   163,   154,   155,   156,   157,   158,
     159,   160,   161,   187,   188,   125,   325,   293,   467,   401,
     172,   173,   174,   126,   323,   258,   400,   563,   523,   524,
     525,   673,   828,   310,   409,   621,   624,   395,   555,   417,
     197,   396,   731,   165,   209,   405,   393,   327,   427,   406,
     413,   394,   769,   394,   414,   180,   183,   186,   394,  -532,
     394,   254,   430,   198,   129,   510,   770,   217,   221,   208,
     138,    26,    27,    26,    27,   593,   594,   595,    26,    27,
      26,    27,    26,    27,   169,   217,   175,   176,   175,   176,
      26,    27,   213,   216,   175,   176,   782,   132,   175,   176,
     141,   611,   175,   176,   911,   832,    26,    27,    34,   150,
     202,   671,   785,   789,   296,   344,   457,   345,   217,   135,
     205,   736,   423,   612,   613,   614,   790,   531,    26,    27,
     458,   241,    34,   877,   807,   217,   251,   218,   457,   456,
     248,   583,  -532,   621,   624,     4,   769,   400,   482,   217,
     466,   222,   465,   817,    34,   907,   166,   409,   395,   905,
     770,   483,   396,   144,    58,   417,   217,   559,   405,   648,
     615,   665,   406,   605,   176,   606,   413,   480,   130,   604,
     414,   561,   255,  -532,   139,  -532,   511,   222,   930,   481,
     782,   816,   538,   671,   534,   175,   176,   170,   324,   542,
     177,   937,   181,   729,  -530,   153,   785,   789,   184,   133,
     314,   677,   211,   943,   142,   393,   214,   665,   314,   218,
     790,   312,   394,   151,   203,   773,   788,   689,   297,   596,
     326,   136,   206,   597,   965,   966,   512,   967,   367,   532,
     394,   252,    26,    27,   607,   550,   551,   471,   955,   956,
     472,   960,   225,   611,   506,   593,   594,   595,    26,    27,
      26,    27,   986,   507,   226,   168,   244,   654,   655,   619,
      26,    27,   245,   620,   164,   612,   613,   614,    28,   932,
     982,   983,   189,   984,    34,    28,   455,   818,   892,   721,
     722,   723,   724,   893,   725,   977,   726,   894,   259,   260,
     947,   980,   190,   570,   571,   572,   573,   574,   950,   242,
     577,   243,   192,   641,   580,   162,    58,   642,   199,   773,
     788,   224,   615,    41,    42,    43,    44,    45,    46,    47,
      48,    49,    50,    51,    52,    53,    54,    55,    56,    57,
     349,   350,    59,    60,   210,   669,   304,   249,   931,   670,
     352,   353,   305,   306,   307,    62,   819,   820,   219,   596,
     544,   545,   546,   597,   821,   514,   515,   822,   489,   824,
     490,   266,   267,   252,   268,   229,    72,   619,    26,    27,
     640,   620,   269,   270,   271,   272,   273,   714,   715,   716,
     717,   718,   719,   661,  -341,  -341,   649,   650,   651,   652,
     653,   355,   356,   656,   522,   641,   660,   358,   359,   642,
     193,   194,   195,   361,   362,   196,   706,   707,   708,   365,
     366,   536,   378,   379,   737,   127,   276,   669,   284,   540,
     279,   670,   381,   382,   391,   392,   232,   125,   403,   404,
     411,   412,   434,   435,   235,   126,   440,   441,   787,   460,
     461,   463,   464,   514,   515,   692,   693,   586,   217,   771,
     695,   696,   238,   772,   867,   457,   901,   902,   915,   916,
     263,   601,   927,   928,   852,   853,   281,   328,   587,   286,
     329,   589,   973,   974,   330,   331,   332,   333,   334,   335,
     336,   337,   338,   339,   791,   340,   294,   341,   342,   885,
     886,   289,   299,   300,   301,   311,   316,   934,   319,    39,
     347,   810,   348,   351,   354,   357,   368,   360,   363,   364,
     372,   632,   373,   637,   608,   374,   879,   427,   808,   880,
    -296,   375,   376,   377,   380,   383,   384,   385,   386,   387,
     388,   389,   787,   390,   402,   410,   430,   470,   425,   424,
     433,   436,   437,   771,   438,   439,   127,   772,   459,   462,
     418,   468,   473,   474,   475,   476,   477,   478,   125,   479,
     811,   812,   484,   485,   878,   486,   126,   487,   488,   492,
     494,   674,   675,   676,   496,   498,   500,   502,   791,   503,
     505,   513,   508,   518,   527,   520,   521,   526,   529,   684,
     685,   686,   687,   552,   554,   565,   553,   558,   566,   567,
     568,   575,   576,   581,   578,   688,   579,   592,   625,   584,
     629,   602,   603,   600,   657,   626,   633,   634,   636,   635,
     646,   679,   698,   661,   711,   713,   705,   868,   869,   681,
     733,   873,   683,   961,   682,   691,   735,   919,   694,   701,
     709,   710,   703,   728,   875,   738,   740,   739,   917,   742,
     805,   806,   918,   809,   814,   813,   830,   732,   981,   827,
     919,   834,   837,   850,   833,   854,  -432,   865,   860,   874,
     872,   917,   864,   890,   881,   918,   882,   883,   897,   899,
     909,   903,   910,   900,   923,   922,   912,   913,   127,   933,
     914,   823,   935,   908,   926,   314,   826,   941,   929,   326,
     394,   939,   953,   963,   951,     5,   971,   497,   946,   949,
     730,   829,   969,   958,   976,   975,   495,   985,   493,   672,
     499,   978,   835,   836,   564,   838,   839,   840,   841,   842,
     843,   844,   845,   846,   847,   848,   849,   979,   987,   569,
     690,   560,   562,   590,   588,   539,   541,   537,   948,   741,
     501,   543,   123,   519,   743,   704,   697,   700,   744,   394,
     863,   528,   420,   957,   936,   938,   891,   535,   610,   659,
     745,   889,   517,   678,   611,   295,   970,   870,     0,    26,
      27,   746,   127,   504,     0,   747,   748,   749,   750,   751,
     752,   753,   754,   755,   322,     0,   612,   756,   757,   758,
       0,     0,     0,     0,     0,    34,     0,     0,   876,     0,
      39,    40,   759,   760,   761,   762,   763,     0,   764,    41,
      42,    43,    44,    45,    46,    47,    48,    49,    50,    51,
      52,    53,    54,    55,    56,    57,   765,    58,    59,    60,
       0,    28,    61,   766,     0,   127,   127,   888,   127,     0,
       0,    62,     0,     0,    63,    64,     0,     0,     0,   887,
       0,     0,     0,     0,    69,   422,   924,    70,     0,     0,
     767,   162,    72,     0,     0,   768,     0,     0,     0,    41,
      42,    43,    44,    45,    46,    47,    48,    49,    50,    51,
      52,    53,    54,    55,    56,    57,     0,     0,    59,    60,
     862,     0,    61,     0,   442,   443,   444,   445,   446,   447,
     448,    62,     0,     0,     0,   940,     0,     0,     6,   952,
       7,     8,     9,    10,    11,    12,   449,    13,    14,    15,
      16,   962,    72,     0,    17,    18,    19,     0,    20,    21,
      22,   972,    23,    24,    25,     0,    26,    27,    28,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    29,    30,    31,
      32,    33,    34,    35,    36,    37,    38,    39,    40,     0,
       0,     0,     0,     0,     0,     0,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,     0,    58,    59,    60,     0,     0,    61,
       0,    26,    27,    28,     0,     0,     0,     0,    62,     0,
       0,    63,    64,    65,    66,    67,    68,     0,     0,     0,
       0,    69,     0,     0,    70,     0,     0,    34,    71,    72,
      73,    74,    39,    40,     0,     0,     0,     0,     0,     0,
       0,    41,    42,    43,    44,    45,    46,    47,    48,    49,
      50,    51,    52,    53,    54,    55,    56,    57,     0,    58,
      59,    60,     0,     0,    61,     0,     0,     0,     0,     0,
       0,     0,     0,    62,     0,     0,    63,    64,     0,   744,
     394,     0,     0,     0,     0,     0,    69,     0,     0,    70,
       0,   745,     0,    71,    72,   611,     0,     0,     0,     0,
      26,    27,   746,     0,     0,     0,   747,   748,   749,   750,
     751,   752,   753,   754,   755,     0,     0,   612,   756,   757,
     758,     0,   647,     0,     0,     0,    34,     0,     0,     0,
       0,    39,    40,   759,   760,   761,   762,   763,     0,   764,
      41,    42,    43,    44,    45,    46,    47,    48,    49,    50,
      51,    52,    53,    54,    55,    56,    57,   765,    58,    59,
      60,     0,     0,    61,   766,     0,    26,    27,    28,     0,
       0,     0,    62,     0,     0,    63,    64,     0,     0,     0,
       0,     0,     0,     0,     0,    69,     0,     0,    70,     0,
       0,   767,    34,    72,     0,     0,   768,    39,    40,     0,
       0,     0,     0,     0,     0,     0,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    28,    58,    59,    60,     0,     0,    61,
       0,     0,     0,     0,     0,     0,     0,     0,    62,     0,
       0,    63,    64,     0,     0,     0,     0,     0,     0,     0,
       0,    69,     0,   162,    70,     0,     0,     0,    71,    72,
       0,    41,    42,    43,    44,    45,    46,    47,    48,    49,
      50,    51,    52,    53,    54,    55,    56,    57,   884,    28,
      59,    60,     0,     0,    61,   766,     0,     0,     0,     0,
       0,     0,     0,    62,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    69,     0,     0,   162,
       0,     0,     0,     0,    72,     0,     0,    41,    42,    43,
      44,    45,    46,    47,    48,    49,    50,    51,    52,    53,
      54,    55,    56,    57,   884,    28,    59,    60,     0,     0,
      61,     0,     0,     0,     0,     0,     0,     0,     0,    62,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    69,     0,     0,   162,     0,     0,     0,     0,
      72,     0,     0,    41,    42,    43,    44,    45,    46,    47,
      48,    49,    50,    51,    52,    53,    54,    55,    56,    57,
      28,     0,    59,    60,     0,     0,    61,     0,     0,     0,
       0,     0,     0,     0,     0,    62,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    69,     0,
     162,     0,     0,     0,     0,    28,    72,     0,    41,    42,
      43,    44,    45,    46,    47,    48,    49,    50,    51,    52,
      53,    54,    55,    56,    57,     0,     0,    59,    60,     0,
       0,    61,     0,     0,     0,   162,     0,     0,     0,     0,
      62,     0,     0,    41,    42,    43,    44,    45,    46,    47,
      48,    49,    50,    51,    52,    53,    54,    55,    56,    57,
       0,    72,    59,    60,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    62,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    72
};

static const yytype_int16 yycheck[] =
{
      12,    13,    14,     3,    25,    17,    18,    19,    20,    21,
      22,    23,    24,    39,    40,     3,   220,   191,   326,   278,
      32,    33,    34,     3,   218,   164,   276,   433,   386,   387,
     388,   592,   731,   207,   284,   508,   508,   276,   425,   289,
      61,   276,   673,    34,    70,   284,     4,   221,    33,   284,
     289,    11,   698,    11,   289,    36,    37,    38,    11,    33,
      11,    33,    33,    63,    33,    33,   698,    92,    33,    69,
      33,    31,    32,    31,    32,    16,    17,    18,    31,    32,
      31,    32,    31,    32,    34,    92,    33,    34,    33,    34,
      31,    32,    73,    74,    33,    34,   698,    35,    33,    34,
      33,    26,    33,    34,    33,   736,    31,    32,    57,    33,
      33,   584,   698,   698,    33,   157,   149,   159,    92,    35,
      35,   682,   296,    48,    49,    50,   698,    35,    31,    32,
     163,   143,    57,   832,   701,    92,   162,   162,   149,   313,
     152,   148,   116,   616,   616,     0,   792,   397,   150,    92,
     324,   116,   163,   720,    57,   875,   147,   407,   397,   874,
     792,   163,   397,    30,    89,   415,    92,   152,   407,   556,
      95,   120,   407,    33,    34,    35,   415,   150,   147,   487,
     415,   152,   154,   157,   147,   159,   154,   116,   908,   162,
     792,   148,   152,   666,   152,    33,    34,   147,   219,   152,
     147,   152,   147,   152,   147,    34,   792,   792,   147,   147,
     210,   152,   147,   928,   147,     4,   147,   120,   218,   162,
     792,   147,    11,   147,   147,   698,   698,   152,   147,   468,
     147,   147,   147,   468,   955,   956,   375,   957,   250,   147,
      11,   158,    31,    32,   104,   419,   420,   147,   945,   946,
     150,   950,   134,    26,   149,    16,    17,    18,    31,    32,
      31,    32,   983,   158,   146,    34,   130,   575,   576,   508,
      31,    32,   136,   508,   147,    48,    49,    50,    33,   910,
     977,   978,    74,   980,    57,    33,   312,    35,   129,   154,
     155,   156,   157,   134,   159,   969,   161,   138,   134,   135,
     931,   975,    33,   442,   443,   444,   445,   446,   939,    30,
     449,    32,    77,   552,   453,    63,    89,   552,    33,   792,
     792,   104,    95,    71,    72,    73,    74,    75,    76,    77,
      78,    79,    80,    81,    82,    83,    84,    85,    86,    87,
     148,   149,    90,    91,   162,   584,   133,    34,   909,   584,
     148,   149,   139,   140,   141,   103,   104,   105,    29,   598,
      64,    65,    66,   598,   112,   113,   114,   115,    33,   727,
      35,   131,   132,   158,   134,   134,   124,   616,    31,    32,
      33,   616,   142,   143,   144,   145,   146,   155,   156,   157,
     158,   159,   160,   147,   148,   149,   570,   571,   572,   573,
     574,   148,   149,   577,   385,   644,   580,   148,   149,   644,
      72,    73,    74,   148,   149,    77,   649,   650,   651,   148,
     149,   402,   148,   149,   683,   425,   151,   666,   151,   410,
     104,   666,   148,   149,   148,   149,   134,   425,   148,   149,
     148,   149,   148,   149,   134,   425,   148,   149,   698,   148,
     149,   148,   149,   113,   114,   148,   149,   457,    92,   698,
     148,   149,   134,   698,   148,   149,   148,   149,   148,   149,
     134,   471,   148,   149,   760,   761,   134,   147,   459,   134,
     150,   462,   965,   966,   154,   155,   156,   157,   158,   159,
     160,   161,   162,   163,   698,   165,    74,   167,   168,   855,
     856,   151,   151,   151,   134,   147,   134,   913,   134,    62,
     150,   705,   150,   150,   150,   150,    33,   150,   150,   150,
      33,   533,    93,   549,   505,   148,   834,    33,   702,   837,
     155,   155,   150,   150,   150,   150,   150,   150,   150,   150,
     150,   150,   792,   150,   150,   150,    33,   148,   151,   157,
     150,   150,   150,   792,   150,   150,   556,   792,   150,   150,
     164,   151,   150,   150,   150,   150,   150,   150,   556,   150,
     709,   710,   166,   150,   833,   150,   556,   147,    94,   104,
      35,   593,   594,   595,    35,    33,    33,    33,   792,   104,
     150,    34,   151,    34,   104,    35,    35,    33,   147,   611,
     612,   613,   614,   151,    33,    35,   153,   153,    35,    35,
      35,   147,   147,   150,   148,   615,   149,   148,    33,   151,
     128,   150,   150,   153,    94,   137,   153,   153,   149,   153,
     148,    16,   151,   147,   117,   661,   147,   811,   812,   148,
      17,   815,   164,   951,   148,   150,   153,   897,   150,   150,
     148,   148,   152,   665,   828,    33,    35,   153,   897,    35,
     153,   153,   897,   153,   150,   147,    18,   679,   976,   153,
     920,   147,   147,    69,   155,   164,   161,   149,   147,   147,
     104,   920,   161,    33,   164,   920,   164,   164,   151,    33,
     148,   165,   148,   867,   153,   147,   150,   150,   698,    33,
     150,   727,    33,   877,   153,   705,   727,    47,   153,   147,
      11,   148,    36,    46,   147,     1,   148,   356,   153,   153,
     666,   733,   153,   165,   147,   153,   353,   148,   350,   591,
     359,   153,   744,   745,   435,   747,   748,   749,   750,   751,
     752,   753,   754,   755,   756,   757,   758,   166,   166,   441,
     616,   428,   431,   464,   461,   407,   412,   404,   932,   693,
     362,   415,     3,   382,   696,   644,   636,   639,    10,    11,
     792,   392,   292,   947,   916,   920,   859,   397,   506,   579,
      22,   858,   379,   598,    26,   197,   960,   813,    -1,    31,
      32,    33,   792,   366,    -1,    37,    38,    39,    40,    41,
      42,    43,    44,    45,   217,    -1,    48,    49,    50,    51,
      -1,    -1,    -1,    -1,    -1,    57,    -1,    -1,   830,    -1,
      62,    63,    64,    65,    66,    67,    68,    -1,    70,    71,
      72,    73,    74,    75,    76,    77,    78,    79,    80,    81,
      82,    83,    84,    85,    86,    87,    88,    89,    90,    91,
      -1,    33,    94,    95,    -1,   855,   856,   857,   858,    -1,
      -1,   103,    -1,    -1,   106,   107,    -1,    -1,    -1,   857,
      -1,    -1,    -1,    -1,   116,   295,   902,   119,    -1,    -1,
     122,    63,   124,    -1,    -1,   127,    -1,    -1,    -1,    71,
      72,    73,    74,    75,    76,    77,    78,    79,    80,    81,
      82,    83,    84,    85,    86,    87,    -1,    -1,    90,    91,
     152,    -1,    94,    -1,    96,    97,    98,    99,   100,   101,
     102,   103,    -1,    -1,    -1,   925,    -1,    -1,     3,   941,
       5,     6,     7,     8,     9,    10,   118,    12,    13,    14,
      15,   953,   124,    -1,    19,    20,    21,    -1,    23,    24,
      25,   963,    27,    28,    29,    -1,    31,    32,    33,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    52,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    71,    72,    73,    74,
      75,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    87,    -1,    89,    90,    91,    -1,    -1,    94,
      -1,    31,    32,    33,    -1,    -1,    -1,    -1,   103,    -1,
      -1,   106,   107,   108,   109,   110,   111,    -1,    -1,    -1,
      -1,   116,    -1,    -1,   119,    -1,    -1,    57,   123,   124,
     125,   126,    62,    63,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    82,    83,    84,    85,    86,    87,    -1,    89,
      90,    91,    -1,    -1,    94,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   103,    -1,    -1,   106,   107,    -1,    10,
      11,    -1,    -1,    -1,    -1,    -1,   116,    -1,    -1,   119,
      -1,    22,    -1,   123,   124,    26,    -1,    -1,    -1,    -1,
      31,    32,    33,    -1,    -1,    -1,    37,    38,    39,    40,
      41,    42,    43,    44,    45,    -1,    -1,    48,    49,    50,
      51,    -1,   152,    -1,    -1,    -1,    57,    -1,    -1,    -1,
      -1,    62,    63,    64,    65,    66,    67,    68,    -1,    70,
      71,    72,    73,    74,    75,    76,    77,    78,    79,    80,
      81,    82,    83,    84,    85,    86,    87,    88,    89,    90,
      91,    -1,    -1,    94,    95,    -1,    31,    32,    33,    -1,
      -1,    -1,   103,    -1,    -1,   106,   107,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   116,    -1,    -1,   119,    -1,
      -1,   122,    57,   124,    -1,    -1,   127,    62,    63,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    71,    72,    73,    74,
      75,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    87,    33,    89,    90,    91,    -1,    -1,    94,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   103,    -1,
      -1,   106,   107,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   116,    -1,    63,   119,    -1,    -1,    -1,   123,   124,
      -1,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    82,    83,    84,    85,    86,    87,    88,    33,
      90,    91,    -1,    -1,    94,    95,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   103,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   116,    -1,    -1,    63,
      -1,    -1,    -1,    -1,   124,    -1,    -1,    71,    72,    73,
      74,    75,    76,    77,    78,    79,    80,    81,    82,    83,
      84,    85,    86,    87,    88,    33,    90,    91,    -1,    -1,
      94,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   103,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   116,    -1,    -1,    63,    -1,    -1,    -1,    -1,
     124,    -1,    -1,    71,    72,    73,    74,    75,    76,    77,
      78,    79,    80,    81,    82,    83,    84,    85,    86,    87,
      33,    -1,    90,    91,    -1,    -1,    94,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   116,    -1,
      63,    -1,    -1,    -1,    -1,    33,   124,    -1,    71,    72,
      73,    74,    75,    76,    77,    78,    79,    80,    81,    82,
      83,    84,    85,    86,    87,    -1,    -1,    90,    91,    -1,
      -1,    94,    -1,    -1,    -1,    63,    -1,    -1,    -1,    -1,
     103,    -1,    -1,    71,    72,    73,    74,    75,    76,    77,
      78,    79,    80,    81,    82,    83,    84,    85,    86,    87,
      -1,   124,    90,    91,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   124
};

  /* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
     symbol of state STATE-NUM.  */
static const yytype_uint16 yystos[] =
{
       0,   170,   171,   172,     0,   171,     3,     5,     6,     7,
       8,     9,    10,    12,    13,    14,    15,    19,    20,    21,
      23,    24,    25,    27,    28,    29,    31,    32,    33,    52,
      53,    54,    55,    56,    57,    58,    59,    60,    61,    62,
      63,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    82,    83,    84,    85,    86,    87,    89,    90,
      91,    94,   103,   106,   107,   108,   109,   110,   111,   116,
     119,   123,   124,   125,   126,   173,   174,   175,   179,   183,
     187,   191,   195,   201,   203,   209,   213,   217,   221,   225,
     228,   229,   233,   237,   241,   248,   255,   265,   269,   270,
     277,   278,   279,   280,   292,   294,   295,   296,   297,   298,
     299,   300,   301,   303,   304,   314,   318,   321,   336,   337,
     341,   342,   345,   347,   348,   376,   398,   402,   406,    33,
     147,   192,    35,   147,   176,    35,   147,   180,    33,   147,
     184,    33,   147,   188,    30,   319,   320,   319,   319,   319,
      33,   147,   315,    34,   319,   319,   319,   319,   319,   319,
     319,   319,    63,   406,   147,    34,   147,   266,    34,    34,
     147,   271,   319,   319,   319,    33,    34,   147,   256,   263,
     263,   147,   242,   263,   147,   249,   263,   336,   336,    74,
      33,   324,    77,    72,    73,    74,    77,   406,   402,    33,
     222,   214,    33,   147,   218,    35,   147,   230,   402,   336,
     162,   147,   234,   263,   147,   238,   263,    92,   162,    29,
     346,    33,   116,   405,   104,   134,   146,   193,   194,   134,
     177,   178,   134,   181,   182,   134,   185,   186,   134,   189,
     190,   319,    30,    32,   130,   136,   316,   317,   319,    34,
     323,   336,   158,   380,    33,   154,   226,   227,   324,   134,
     135,   267,   268,   134,   272,   273,   131,   132,   134,   142,
     143,   144,   145,   146,   258,   259,   151,   260,   257,   104,
     264,   134,   243,   244,   151,   245,   134,   250,   251,   151,
     252,   349,   343,   380,    74,   405,    33,   147,   210,   151,
     151,   134,   219,   220,   133,   139,   140,   141,   231,   232,
     380,   147,   147,   196,   402,   407,   134,   235,   236,   134,
     239,   240,   337,   407,   406,   348,   147,   380,   147,   150,
     154,   155,   156,   157,   158,   159,   160,   161,   162,   163,
     165,   167,   168,   377,   157,   159,   404,   150,   150,   148,
     149,   150,   148,   149,   150,   148,   149,   150,   148,   149,
     150,   148,   149,   150,   150,   148,   149,   319,    33,   381,
     382,   202,    33,    93,   148,   155,   150,   150,   148,   149,
     150,   148,   149,   150,   150,   150,   150,   150,   150,   150,
     150,   148,   149,     4,    11,   225,   228,   261,   262,   305,
     309,   264,   150,   148,   149,   225,   228,   246,   247,   309,
     150,   148,   149,   225,   228,   253,   254,   309,   164,   351,
     351,   322,   404,   380,   157,   151,   211,    33,   223,   224,
      33,   215,   216,   150,   148,   149,   150,   150,   150,   150,
     148,   149,    96,    97,    98,    99,   100,   101,   102,   118,
     387,   388,   389,   402,   403,   336,   380,   149,   163,   150,
     148,   149,   150,   148,   149,   163,   380,   387,   151,   399,
     148,   147,   150,   150,   150,   150,   150,   150,   150,   150,
     150,   162,   150,   163,   166,   150,   150,   147,    94,    33,
      35,   365,   104,   194,    35,   178,    35,   182,    33,   186,
      33,   190,    33,   104,   317,   150,   149,   158,   151,   205,
      33,   154,   324,    34,   113,   114,   338,   268,    34,   273,
      35,    35,   263,   338,   338,   338,    33,   104,   259,   147,
     306,    35,   147,   310,   152,   262,   263,   244,   152,   247,
     263,   251,   152,   254,    64,    65,    66,   352,   353,   354,
     380,   380,   151,   153,    33,   174,   212,   347,   153,   152,
     224,   152,   216,   365,   220,    35,    35,    35,    35,   232,
     324,   324,   324,   324,   324,   147,   147,   324,   148,   149,
     324,   150,   330,   148,   151,   197,   402,   263,   236,   263,
     240,   204,   148,    16,    17,    18,   225,   228,   400,   401,
     153,   402,   150,   150,   387,    33,    35,   104,   263,   383,
     382,    26,    48,    49,    50,    95,   206,   207,   208,   225,
     228,   280,   289,   293,   321,    33,   137,   307,   308,   128,
     311,   312,   319,   153,   153,   153,   149,   336,   350,   344,
      33,   225,   228,   325,   326,   327,   148,   152,   174,   380,
     380,   380,   380,   380,   387,   387,   380,    94,   378,   389,
     380,   147,   331,   334,   335,   120,   198,   199,   200,   225,
     228,   280,   205,   378,   319,   319,   319,   152,   401,    16,
     274,   148,   148,   164,   319,   319,   319,   319,   402,   152,
     207,   150,   148,   149,   150,   148,   149,   353,   151,   355,
     355,   150,   329,   152,   327,   147,   330,   330,   330,   148,
     148,   117,   408,   336,   155,   156,   157,   158,   159,   160,
     332,   154,   155,   156,   157,   159,   161,   333,   319,   152,
     199,   408,   319,    17,   275,   153,   378,   264,    33,   153,
      35,   308,    35,   312,    10,    22,    33,    37,    38,    39,
      40,    41,    42,    43,    44,    45,    49,    50,    51,    64,
      65,    66,    67,    68,    70,    88,    95,   122,   127,   195,
     209,   225,   228,   280,   281,   282,   283,   284,   285,   286,
     287,   288,   289,   290,   291,   293,   302,   309,   321,   341,
     342,   348,   356,   357,   358,   367,   368,   370,   375,   376,
     390,   393,   395,   396,   398,   153,   153,   334,   380,   153,
     407,   324,   324,   147,   150,   379,   148,   334,    35,   104,
     105,   112,   115,   336,   338,   339,   406,   153,   379,   319,
      18,   276,   408,   155,   147,   319,   319,   147,   319,   319,
     319,   319,   319,   319,   319,   319,   319,   319,   319,   319,
      69,   366,   366,   366,   164,   391,   392,   397,   394,   369,
     147,   359,   152,   357,   161,   149,   328,   148,   380,   380,
     336,   409,   104,   380,   147,   380,   319,   379,   264,   387,
     387,   164,   164,   164,    88,   393,   393,   376,   402,   395,
      33,   370,   129,   134,   138,   360,   361,   151,   362,    33,
     380,   148,   149,   165,   373,   331,   340,   373,   380,   148,
     148,    33,   150,   150,   150,   148,   149,   225,   228,   309,
     363,   364,   147,   153,   336,   374,   153,   148,   149,   153,
     373,   378,   408,    33,   365,    33,   361,   152,   364,   148,
     402,    47,   385,   331,   309,   313,   153,   408,   380,   153,
     408,   147,   319,    36,   386,   385,   385,   380,   165,   371,
     379,   387,   319,    46,   384,   386,   386,   373,   372,   153,
     380,   148,   319,   384,   384,   153,   147,   313,   153,   166,
     313,   387,   385,   385,   385,   148,   386,   166
};

  /* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint16 yyr1[] =
{
       0,   169,   170,   170,   172,   171,   173,   173,   173,   173,
     173,   173,   173,   173,   173,   173,   173,   173,   173,   173,
     173,   173,   173,   173,   173,   173,   173,   173,   173,   173,
     173,   173,   173,   173,   173,   173,   173,   173,   173,   173,
     173,   173,   174,   174,   174,   174,   174,   174,   174,   174,
     174,   174,   174,   174,   175,   176,   176,   177,   177,   178,
     179,   180,   180,   181,   181,   182,   183,   184,   184,   185,
     185,   186,   187,   188,   188,   189,   189,   190,   191,   192,
     192,   193,   193,   194,   194,   195,   196,   196,   197,   198,
     198,   199,   199,   199,   199,   200,   202,   201,   204,   203,
     205,   206,   206,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   208,   210,   209,   211,   211,   212,   212,   214,
     213,   215,   215,   216,   217,   218,   218,   219,   219,   220,
     222,   221,   223,   223,   224,   225,   226,   226,   226,   226,
     227,   227,   228,   229,   230,   230,   230,   231,   231,   232,
     232,   232,   232,   233,   234,   234,   235,   235,   236,   237,
     238,   238,   239,   239,   240,   241,   242,   242,   243,   243,
     244,   245,   245,   246,   246,   247,   247,   247,   248,   249,
     249,   250,   250,   251,   252,   252,   253,   253,   254,   254,
     254,   255,   255,   257,   256,   256,   258,   258,   259,   259,
     259,   259,   259,   259,   259,   259,   260,   260,   261,   261,
     262,   262,   262,   262,   263,   263,   264,   264,   265,   266,
     266,   267,   267,   268,   268,   269,   270,   271,   271,   272,
     272,   273,   274,   274,   275,   275,   276,   276,   277,   278,
     279,   280,   281,   282,   283,   284,   285,   286,   287,   288,
     289,   290,   291,   292,   293,   294,   295,   296,   297,   298,
     299,   300,   301,   302,   303,   304,   305,   306,   307,   307,
     308,   309,   310,   310,   310,   311,   311,   312,   313,   313,
     314,   315,   315,   316,   316,   317,   317,   318,   319,   320,
     320,   322,   321,   323,   323,   324,   324,   325,   325,   326,
     326,   327,   327,   327,   328,   328,   329,   329,   330,   330,
     331,   331,   332,   332,   332,   332,   332,   332,   333,   333,
     333,   333,   333,   333,   333,   334,   335,   335,   336,   336,
     337,   338,   338,   339,   339,   339,   339,   339,   339,   339,
     339,   340,   340,   340,   341,   341,   343,   344,   342,   346,
     345,   347,   349,   350,   348,   351,   351,   352,   352,   353,
     354,   354,   354,   354,   355,   355,   356,   356,   357,   357,
     357,   357,   357,   357,   357,   357,   357,   357,   357,   357,
     357,   357,   357,   357,   357,   357,   357,   357,   357,   357,
     357,   357,   357,   357,   357,   357,   357,   357,   357,   357,
     357,   357,   358,   359,   360,   360,   361,   361,   361,   362,
     362,   363,   363,   364,   364,   364,   365,   365,   366,   366,
     367,   369,   368,   368,   370,   371,   372,   371,   373,   374,
     373,   375,   375,   376,   376,   376,   376,   377,   377,   377,
     377,   377,   377,   377,   377,   377,   377,   377,   377,   377,
     377,   377,   377,   377,   377,   377,   377,   377,   377,   377,
     377,   377,   377,   377,   377,   377,   378,   378,   379,   379,
     380,   380,   381,   381,   382,   382,   383,   383,   383,   383,
     384,   384,   385,   385,   386,   386,   387,   388,   388,   388,
     389,   389,   389,   389,   389,   389,   389,   389,   389,   391,
     390,   392,   390,   390,   394,   393,   393,   395,   395,   397,
     396,   396,   398,   399,   399,   400,   400,   401,   401,   401,
     401,   401,   402,   402,   403,   404,   404,   405,   405,   405,
     406,   406,   406,   406,   406,   406,   406,   406,   406,   406,
     406,   406,   406,   406,   406,   406,   406,   406,   406,   406,
     406,   406,   406,   406,   406,   406,   406,   406,   406,   406,
     407,   407,   408,   408,   409,   409,   409
};

  /* YYR2[YYN] -- Number of symbols on the right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     1,     2,     0,     2,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     2,     1,     3,     1,     3,     3,
       2,     1,     3,     1,     3,     3,     2,     1,     3,     1,
       3,     3,     3,     1,     3,     1,     3,     3,     2,     2,
       3,     1,     3,     3,     3,     5,     0,     3,     4,     1,
       2,     1,     1,     1,     1,     2,     0,     5,     0,     6,
       4,     1,     2,     1,     1,     1,     1,     2,     2,     1,
       1,     1,    13,     0,     5,     0,     3,     1,     2,     0,
       5,     1,     2,     1,     2,     1,     3,     1,     3,     3,
       0,     5,     1,     2,     1,     4,     1,     2,     3,     4,
       1,     3,     1,     3,     0,     1,     3,     1,     3,     3,
       3,     3,     3,     2,     1,     3,     1,     3,     3,     2,
       1,     3,     1,     3,     3,     3,     1,     3,     1,     3,
       3,     0,     4,     1,     2,     1,     1,     1,     3,     1,
       3,     1,     3,     3,     0,     4,     1,     2,     1,     1,
       1,     3,     3,     0,     3,     3,     1,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     0,     4,     1,     2,
       1,     1,     1,     1,     1,     1,     0,     1,     2,     1,
       3,     1,     3,     3,     3,     2,     2,     1,     3,     1,
       3,     3,     0,     2,     0,     2,     0,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     3,     1,     3,
       3,     3,     0,     1,     3,     1,     3,     3,     0,     1,
       3,     1,     3,     1,     3,     3,     3,     4,     2,     1,
       2,     0,     8,     0,     1,     0,     1,     0,     1,     1,
       2,     1,     1,     4,     0,     1,     0,     2,     0,     2,
       1,     3,     1,     1,     1,     1,     1,     1,     0,     1,
       1,     1,     1,     1,     1,     3,     0,     3,     1,     3,
       1,     1,     1,     1,     4,     1,     1,     1,     1,     1,
       1,     0,     1,     3,     5,    11,     0,     0,     8,     0,
       3,     4,     0,     0,     8,     0,     2,     1,     3,     2,
       0,     1,     1,     1,     0,     3,     1,     2,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     2,     2,     2,     3,     3,
       3,     2,     3,     3,     1,     3,     3,     3,     3,     0,
       4,     1,     2,     1,     1,     1,     1,     1,     0,     1,
      11,     0,     3,     1,    10,     0,     0,     6,     0,     0,
       7,     0,     1,    15,     7,    15,    14,     1,     1,     1,
       1,     1,     1,     1,     1,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     3,     3,     1,     2,     2,
       1,     2,     2,     2,     1,     2,     0,     1,     0,     2,
       0,     3,     1,     3,     1,     3,     1,     5,     1,     1,
       0,     2,     0,     2,     0,     2,     1,     0,     1,     3,
       4,     4,     4,     3,     3,     6,     6,     3,     2,     0,
       3,     0,     3,     1,     0,     3,     1,     1,     1,     0,
       3,     1,     8,     0,     3,     1,     2,     1,     1,     2,
       2,     2,     4,     3,     3,     0,     1,     0,     3,     2,
       1,     4,     2,     2,     1,     1,     2,     1,     1,     2,
       2,     3,     1,     1,     1,     2,     2,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     3,     0,     4,     0,     1,     3
};


#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)
#define YYEMPTY         (-2)
#define YYEOF           0

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                  \
do                                                              \
  if (yychar == YYEMPTY)                                        \
    {                                                           \
      yychar = (Token);                                         \
      yylval = (Value);                                         \
      YYPOPSTACK (yylen);                                       \
      yystate = *yyssp;                                         \
      goto yybackup;                                            \
    }                                                           \
  else                                                          \
    {                                                           \
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;                                                  \
    }                                                           \
while (0)

/* Error token number */
#define YYTERROR        1
#define YYERRCODE       256



/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)

/* This macro is provided for backward compatibility. */
#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


# define YY_SYMBOL_PRINT(Title, Type, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Type, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*----------------------------------------.
| Print this symbol's value on YYOUTPUT.  |
`----------------------------------------*/

static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  FILE *yyo = yyoutput;
  YYUSE (yyo);
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# endif
  YYUSE (yytype);
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyoutput, "%s %s (",
             yytype < YYNTOKENS ? "token" : "nterm", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yytype_int16 *yybottom, yytype_int16 *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yytype_int16 *yyssp, YYSTYPE *yyvsp, int yyrule)
{
  unsigned long int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       yystos[yyssp[yyi + 1 - yynrhs]],
                       &(yyvsp[(yyi + 1) - (yynrhs)])
                                              );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
static YYSIZE_T
yystrlen (const char *yystr)
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
yystpcpy (char *yydest, const char *yysrc)
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
        switch (*++yyp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++yyp != '\\')
              goto do_not_strip_quotes;
            /* Fall through.  */
          default:
            if (yyres)
              yyres[yyn] = *yyp;
            yyn++;
            break;

          case '"':
            if (yyres)
              yyres[yyn] = '\0';
            return yyn;
          }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYSIZE_T *yymsg_alloc, char **yymsg,
                yytype_int16 *yyssp, int yytoken)
{
  YYSIZE_T yysize0 = yytnamerr (YY_NULLPTR, yytname[yytoken]);
  YYSIZE_T yysize = yysize0;
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULLPTR;
  /* Arguments of yyformat. */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Number of reported tokens (one for the "unexpected", one per
     "expected"). */
  int yycount = 0;

  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[*yyssp];
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                {
                  YYSIZE_T yysize1 = yysize + yytnamerr (YY_NULLPTR, yytname[yyx]);
                  if (! (yysize <= yysize1
                         && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
                    return 2;
                  yysize = yysize1;
                }
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    YYSIZE_T yysize1 = yysize + yystrlen (yyformat);
    if (! (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
      return 2;
    yysize = yysize1;
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          yyp++;
          yyformat++;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
{
  YYUSE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}




/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    int yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       'yyss': related to states.
       'yyvs': related to semantic values.

       Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yytype_int16 yyssa[YYINITDEPTH];
    yytype_int16 *yyss;
    yytype_int16 *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYSIZE_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yyssp = yyss = yyssa;
  yyvsp = yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */
  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        YYSTYPE *yyvs1 = yyvs;
        yytype_int16 *yyss1 = yyss;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * sizeof (*yyssp),
                    &yyvs1, yysize * sizeof (*yyvsp),
                    &yystacksize);

        yyss = yyss1;
        yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yytype_int16 *yyss1 = yyss;
        union yyalloc *yyptr =
          (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
        if (! yyptr)
          goto yyexhaustedlab;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
                  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token.  */
  yychar = YYEMPTY;

  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 4:
#line 550 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /*
             * We don't do these in parserEOF() because the parser is reading
             * ahead and that would be too early.
             */

            if (previousFile != NULL)
            {
                handleEOF();

                if (currentContext.prevmod != NULL)
                    handleEOM();

                free(previousFile);
                previousFile = NULL;
            }
    }
#line 2647 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 53:
#line 618 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope == NULL)
                    yyerror("%TypeHeaderCode can only be used in a namespace, class or mapped type");

                appendCodeBlock(&scope->iff->hdrcode, (yyvsp[0].codeb));
            }
        }
#line 2663 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 54:
#line 631 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                currentModule->defdocstring = convertFormat((yyvsp[0].defdocstring).name);
        }
#line 2672 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 55:
#line 637 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            (yyval.defdocstring).name = (yyvsp[0].text);
        }
#line 2682 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 56:
#line 642 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.defdocstring) = (yyvsp[-1].defdocstring);
        }
#line 2690 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 58:
#line 648 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.defdocstring) = (yyvsp[-2].defdocstring);

            switch ((yyvsp[0].defdocstring).token)
            {
            case TK_NAME: (yyval.defdocstring).name = (yyvsp[0].defdocstring).name; break;
            }
        }
#line 2703 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 59:
#line 658 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.defdocstring).token = TK_NAME;

            (yyval.defdocstring).name = (yyvsp[0].text);
        }
#line 2713 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 60:
#line 665 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                if ((currentModule->encoding = convertEncoding((yyvsp[0].defencoding).name)) == no_type)
                    yyerror("The %DefaultEncoding name must be one of \"ASCII\", \"Latin-1\", \"UTF-8\" or \"None\"");
            }
        }
#line 2725 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 61:
#line 674 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            (yyval.defencoding).name = (yyvsp[0].text);
        }
#line 2735 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 62:
#line 679 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.defencoding) = (yyvsp[-1].defencoding);
        }
#line 2743 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 64:
#line 685 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.defencoding) = (yyvsp[-2].defencoding);

            switch ((yyvsp[0].defencoding).token)
            {
            case TK_NAME: (yyval.defencoding).name = (yyvsp[0].defencoding).name; break;
            }
        }
#line 2756 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 65:
#line 695 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.defencoding).token = TK_NAME;

            (yyval.defencoding).name = (yyvsp[0].text);
        }
#line 2766 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 66:
#line 702 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* Note that %Plugin is internal in SIP v4. */

            if (notSkipping())
                appendString(&currentSpec->plugins, (yyvsp[0].plugin).name);
        }
#line 2777 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 67:
#line 710 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            (yyval.plugin).name = (yyvsp[0].text);
        }
#line 2787 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 68:
#line 715 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.plugin) = (yyvsp[-1].plugin);
        }
#line 2795 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 70:
#line 721 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.plugin) = (yyvsp[-2].plugin);

            switch ((yyvsp[0].plugin).token)
            {
            case TK_NAME: (yyval.plugin).name = (yyvsp[0].plugin).name; break;
            }
        }
#line 2808 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 71:
#line 731 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.plugin).token = TK_NAME;

            (yyval.plugin).name = (yyvsp[0].text);
        }
#line 2818 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 72:
#line 738 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if ((yyvsp[-1].veh).name == NULL)
                yyerror("%VirtualErrorHandler must have a 'name' argument");

            if (notSkipping())
            {
                virtErrorHandler *veh, **tailp;

                /* Check there isn't already a handler with the same name. */
                for (tailp = &currentSpec->errorhandlers; (veh = *tailp) != NULL; tailp = &veh->next)
                    if (strcmp(veh->name, (yyvsp[-1].veh).name) == 0)
                        break;

                if (veh != NULL)
                    yyerror("A virtual error handler with that name has already been defined");

                veh = sipMalloc(sizeof (virtErrorHandler));

                veh->name = (yyvsp[-1].veh).name;
                appendCodeBlock(&veh->code, (yyvsp[0].codeb));
                veh->mod = currentModule;
                veh->index = currentModule->nrvirterrorhandlers++;
                veh->next = NULL;

                *tailp = veh;
            }
        }
#line 2850 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 73:
#line 767 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            (yyval.veh).name = (yyvsp[0].text);
        }
#line 2860 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 74:
#line 772 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.veh) = (yyvsp[-1].veh);
        }
#line 2868 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 76:
#line 778 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.veh) = (yyvsp[-2].veh);

            switch ((yyvsp[0].veh).token)
            {
            case TK_NAME: (yyval.veh).name = (yyvsp[0].veh).name; break;
            }
        }
#line 2881 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 77:
#line 788 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.veh).token = TK_NAME;

            (yyval.veh).name = (yyvsp[0].text);
        }
#line 2891 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 78:
#line 795 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                apiVersionRangeDef *avd;

                if (findAPI(currentSpec, (yyvsp[0].api).name) != NULL)
                    yyerror("The API name in the %API directive has already been defined");

                if ((yyvsp[0].api).version < 1)
                    yyerror("The version number in the %API directive must be greater than or equal to 1");

                avd = sipMalloc(sizeof (apiVersionRangeDef));

                avd->api_name = cacheName(currentSpec, (yyvsp[0].api).name);
                avd->from = (yyvsp[0].api).version;
                avd->to = -1;

                avd->next = currentModule->api_versions;
                currentModule->api_versions = avd;

                if (inMainModule())
                    setIsUsedName(avd->api_name);
            }
        }
#line 2920 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 79:
#line 821 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            deprecated("%API name and version number should be specified using the 'name' and 'version' arguments");

            (yyval.api).name = (yyvsp[-1].text);
            (yyval.api).version = (yyvsp[0].number);
        }
#line 2933 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 80:
#line 829 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.api) = (yyvsp[-1].api);
        }
#line 2941 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 82:
#line 835 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.api) = (yyvsp[-2].api);

            switch ((yyvsp[0].api).token)
            {
            case TK_NAME: (yyval.api).name = (yyvsp[0].api).name; break;
            case TK_VERSION: (yyval.api).version = (yyvsp[0].api).version; break;
            }
        }
#line 2955 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 83:
#line 846 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.api).token = TK_NAME;

            (yyval.api).name = (yyvsp[0].text);
            (yyval.api).version = 0;
        }
#line 2966 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 84:
#line 852 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.api).token = TK_VERSION;

            (yyval.api).name = NULL;
            (yyval.api).version = (yyvsp[0].number);
        }
#line 2977 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 85:
#line 860 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                static const char *annos[] = {
                    "Default",
                    "PyName",
                    NULL
                };

                exceptionDef *xd;
                const char *pyname;

                checkAnnos(&(yyvsp[-1].optflags), annos);

                if (currentSpec->genc)
                    yyerror("%Exception not allowed in a C module");

                if ((yyvsp[0].exception).raise_code == NULL)
                    yyerror("%Exception must have a %RaiseCode sub-directive");

                pyname = getPythonName(currentModule, &(yyvsp[-1].optflags), scopedNameTail((yyvsp[-3].scpvalp)));

                checkAttributes(currentSpec, currentModule, NULL, NULL,
                        pyname, FALSE);

                xd = findException(currentSpec, (yyvsp[-3].scpvalp), TRUE);

                if (xd->cd != NULL)
                    yyerror("%Exception name has already been seen as a class name - it must be defined before being used");

                if (xd->iff->module != NULL)
                    yyerror("The %Exception has already been defined");

                /* Complete the definition. */
                xd->iff->module = currentModule;
                appendCodeBlock(&xd->iff->hdrcode, (yyvsp[0].exception).type_header_code);
                xd->pyname = pyname;
                xd->bibase = (yyvsp[-2].exceptionbase).bibase;
                xd->base = (yyvsp[-2].exceptionbase).base;
                appendCodeBlock(&xd->raisecode, (yyvsp[0].exception).raise_code);

                if (getOptFlag(&(yyvsp[-1].optflags), "Default", bool_flag) != NULL)
                    currentModule->defexception = xd;

                if (xd->bibase != NULL || xd->base != NULL)
                    xd->exceptionnr = currentModule->nrexceptions++;
            }
        }
#line 3030 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 86:
#line 910 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.exceptionbase).bibase = NULL;
            (yyval.exceptionbase).base = NULL;
        }
#line 3039 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 87:
#line 914 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            exceptionDef *xd;

            (yyval.exceptionbase).bibase = NULL;
            (yyval.exceptionbase).base = NULL;

            /* See if it is a defined exception. */
            for (xd = currentSpec->exceptions; xd != NULL; xd = xd->next)
                if (compareScopedNames(xd->iff->fqcname, (yyvsp[-1].scpvalp)) == 0)
                {
                    (yyval.exceptionbase).base = xd;
                    break;
                }

            if (xd == NULL && (yyvsp[-1].scpvalp)->next == NULL && strncmp((yyvsp[-1].scpvalp)->name, "SIP_", 4) == 0)
            {
                /* See if it is a builtin exception. */

                static char *builtins[] = {
                    "BaseException",
                    "Exception",
                    "StopIteration",
                    "GeneratorExit",
                    "ArithmeticError",
                    "LookupError",
                    "StandardError",                /* Python v2. */

                    "AssertionError",
                    "AttributeError",
                    "BufferError",
                    "EOFError",
                    "FloatingPointError",
                    "OSError",
                    "ImportError",
                    "IndexError",
                    "KeyError",
                    "KeyboardInterrupt",
                    "MemoryError",
                    "NameError",
                    "OverflowError",
                    "RuntimeError",
                    "NotImplementedError",
                    "SyntaxError",
                    "IndentationError",
                    "TabError",
                    "ReferenceError",
                    "SystemError",
                    "SystemExit",
                    "TypeError",
                    "UnboundLocalError",
                    "UnicodeError",
                    "UnicodeEncodeError",
                    "UnicodeDecodeError",
                    "UnicodeTranslateError",
                    "ValueError",
                    "ZeroDivisionError",
                    "EnvironmentError",             /* Python v2. */
                    "IOError",                      /* Python v2. */
                    "WindowsError",                 /* Python v2. */
                    "VMSError",                     /* Python v2. */

                    "BlockingIOError",
                    "BrokenPipeError",
                    "ChildProcessError",
                    "ConnectionError",
                    "ConnectionAbortedError",
                    "ConnectionRefusedError",
                    "ConnectionResetError",
                    "FileExistsError",
                    "FileNotFoundError",
                    "InterruptedError",
                    "IsADirectoryError",
                    "NotADirectoryError",
                    "PermissionError",
                    "ProcessLookupError",
                    "TimeoutError",

                    "Warning",
                    "UserWarning",
                    "DeprecationWarning",
                    "PendingDeprecationWarning",
                    "SyntaxWarning",
                    "RuntimeWarning",
                    "FutureWarning",
                    "ImportWarning",
                    "UnicodeWarning",
                    "BytesWarning",
                    "ResourceWarning",

                    NULL
                };

                char **cp;

                for (cp = builtins; *cp != NULL; ++cp)
                    if (strcmp((yyvsp[-1].scpvalp)->name + 4, *cp) == 0)
                    {
                        (yyval.exceptionbase).bibase = *cp;
                        break;
                    }
            }

            if ((yyval.exceptionbase).bibase == NULL && (yyval.exceptionbase).base == NULL)
                yyerror("Unknown exception base type");
        }
#line 3149 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 88:
#line 1021 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.exception) = (yyvsp[-2].exception);
        }
#line 3157 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 90:
#line 1027 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.exception) = (yyvsp[-1].exception);

            switch ((yyvsp[0].exception).token)
            {
            case TK_RAISECODE: (yyval.exception).raise_code = (yyvsp[0].exception).raise_code; break;
            case TK_TYPEHEADERCODE: (yyval.exception).type_header_code = (yyvsp[0].exception).type_header_code; break;
            }
        }
#line 3171 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 91:
#line 1038 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.exception).token = TK_IF;
        }
#line 3179 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 92:
#line 1041 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.exception).token = TK_END;
        }
#line 3187 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 93:
#line 1044 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                (yyval.exception).token = TK_RAISECODE;
                (yyval.exception).raise_code = (yyvsp[0].codeb);
            }
            else
            {
                (yyval.exception).token = 0;
                (yyval.exception).raise_code = NULL;
            }

            (yyval.exception).type_header_code = NULL;
        }
#line 3206 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 94:
#line 1058 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                (yyval.exception).token = TK_TYPEHEADERCODE;
                (yyval.exception).type_header_code = (yyvsp[0].codeb);
            }
            else
            {
                (yyval.exception).token = 0;
                (yyval.exception).type_header_code = NULL;
            }

            (yyval.exception).raise_code = NULL;
        }
#line 3225 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 95:
#line 1074 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 3233 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 96:
#line 1079 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                static const char *annos[] = {
                    "AllowNone",
                    "API",
                    "DocType",
                    "NoRelease",
                    "PyName",
                    "TypeHint",
                    "TypeHintIn",
                    "TypeHintOut",
                    "TypeHintValue",
                    NULL
                };

                checkAnnos(&(yyvsp[0].optflags), annos);

                currentMappedType = newMappedType(currentSpec, &(yyvsp[-1].memArg), &(yyvsp[0].optflags));
            }
        }
#line 3259 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 98:
#line 1102 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                static const char *annos[] = {
                    "AllowNone",
                    "DocType",
                    "NoRelease",
                    "TypeHint",
                    "TypeHintIn",
                    "TypeHintOut",
                    "TypeHintValue",
                    NULL
                };

                int a;
                mappedTypeTmplDef *mtt;
                ifaceFileDef *iff;

                checkAnnos(&(yyvsp[0].optflags), annos);

                if (currentSpec->genc)
                    yyerror("%MappedType templates not allowed in a C module");

                /*
                 * Check the template arguments are basic types or simple
                 * names.
                 */
                for (a = 0; a < (yyvsp[-3].signature).nrArgs; ++a)
                {
                    argDef *ad = &(yyvsp[-3].signature).args[a];

                    if (ad->atype == defined_type && ad->u.snd->next != NULL)
                        yyerror("%MappedType template arguments must be simple names");
                }

                if ((yyvsp[-1].memArg).atype != template_type)
                    yyerror("%MappedType template must map a template type");

                /* Check a template hasn't already been provided. */
                for (mtt = currentSpec->mappedtypetemplates; mtt != NULL; mtt = mtt->next)
                    if (compareScopedNames(mtt->mt->type.u.td->fqname, (yyvsp[-1].memArg).u.td->fqname) == 0 && sameTemplateSignature(&mtt->mt->type.u.td->types, &(yyvsp[-1].memArg).u.td->types, TRUE))
                        yyerror("%MappedType template for this type has already been defined");

                (yyvsp[-1].memArg).nrderefs = 0;
                (yyvsp[-1].memArg).argflags = 0;

                mtt = sipMalloc(sizeof (mappedTypeTmplDef));

                mtt->sig = (yyvsp[-3].signature);
                mtt->mt = allocMappedType(currentSpec, &(yyvsp[-1].memArg));
                mappedTypeAnnos(mtt->mt, &(yyvsp[0].optflags));
                mtt->next = currentSpec->mappedtypetemplates;

                currentSpec->mappedtypetemplates = mtt;

                currentMappedType = mtt->mt;

                /* Create a dummy interface file. */
                iff = sipMalloc(sizeof (ifaceFileDef));
                iff->hdrcode = NULL;
                mtt->mt->iff = iff;
            }
        }
#line 3327 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 100:
#line 1167 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                if (currentMappedType->convfromcode == NULL)
                    yyerror("%MappedType must have a %ConvertFromTypeCode directive");

                if (currentMappedType->convtocode == NULL)
                    yyerror("%MappedType must have a %ConvertToTypeCode directive");

                currentMappedType = NULL;
            }
        }
#line 3344 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 105:
#line 1187 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentMappedType->iff->hdrcode, (yyvsp[0].codeb));
        }
#line 3353 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 106:
#line 1191 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentMappedType->typecode, (yyvsp[0].codeb));
        }
#line 3362 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 107:
#line 1195 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                if (currentMappedType->convfromcode != NULL)
                    yyerror("%MappedType has more than one %ConvertFromTypeCode directive");

                appendCodeBlock(&currentMappedType->convfromcode, (yyvsp[0].codeb));
            }
        }
#line 3376 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 108:
#line 1204 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                if (currentMappedType->convtocode != NULL)
                    yyerror("%MappedType has more than one %ConvertToTypeCode directive");

                appendCodeBlock(&currentMappedType->convtocode, (yyvsp[0].codeb));
            }
        }
#line 3390 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 109:
#line 1213 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                if (currentMappedType->instancecode != NULL)
                    yyerror("%MappedType has more than one %InstanceCode directive");

                appendCodeBlock(&currentMappedType->instancecode, (yyvsp[0].codeb));
            }
        }
#line 3404 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 112:
#line 1226 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                applyTypeFlags(currentModule, &(yyvsp[-11].memArg), &(yyvsp[-4].optflags));

                (yyvsp[-8].signature).result = (yyvsp[-11].memArg);

                newFunction(currentSpec, currentModule, NULL,
                        currentMappedType, 0, TRUE, FALSE, FALSE, FALSE, (yyvsp[-10].text),
                        &(yyvsp[-8].signature), (yyvsp[-6].number), FALSE, &(yyvsp[-4].optflags), (yyvsp[0].codeb), NULL, NULL, (yyvsp[-5].throwlist), (yyvsp[-3].optsignature), (yyvsp[-1].codeb));
            }
        }
#line 3421 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 113:
#line 1240 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (currentSpec -> genc)
                yyerror("namespace definition not allowed in a C module");

            if (notSkipping())
            {
                classDef *ns, *c_scope;
                ifaceFileDef *scope;

                if ((c_scope = currentScope()) != NULL)
                    scope = c_scope->iff;
                else
                    scope = NULL;

                ns = newClass(currentSpec, namespace_iface, NULL,
                        text2scopedName(scope, (yyvsp[0].text)), NULL, NULL, NULL, NULL);

                pushScope(ns);

                sectionFlags = 0;
            }
        }
#line 3448 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 114:
#line 1261 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                if (inMainModule())
                {
                    classDef *ns = currentScope();

                    setIsUsedName(ns->iff->name);
                    setIsUsedName(ns->pyname);
                }

                popScope();
            }
        }
#line 3467 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 119:
#line 1285 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                qualDef *qd;

                for (qd = currentModule->qualifiers; qd != NULL; qd = qd->next)
                    if (qd->qtype == platform_qualifier)
                        yyerror("%Platforms has already been defined for this module");
            }
        }
#line 3482 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 120:
#line 1295 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                qualDef *qd;
                int nrneeded;

                /* Check that exactly one platform in the set was requested. */
                nrneeded = 0;

                for (qd = currentModule->qualifiers; qd != NULL; qd = qd->next)
                    if (qd->qtype == platform_qualifier && selectedQualifier(neededQualifiers, qd))
                        ++nrneeded;

                if (nrneeded > 1)
                    yyerror("No more than one of these %Platforms must be specified with the -t flag");
            }
        }
#line 3504 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 123:
#line 1318 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            newQualifier(currentModule, -1, -1, notSkipping(), (yyvsp[0].text),
                    platform_qualifier);
        }
#line 3513 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 124:
#line 1324 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            newQualifier(currentModule, -1, -1, notSkipping(), (yyvsp[0].feature).name,
                    feature_qualifier);
        }
#line 3522 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 125:
#line 1330 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            (yyval.feature).name = (yyvsp[0].text);
        }
#line 3532 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 126:
#line 1335 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.feature) = (yyvsp[-1].feature);
        }
#line 3540 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 128:
#line 1341 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.feature) = (yyvsp[-2].feature);

            switch ((yyvsp[0].feature).token)
            {
            case TK_NAME: (yyval.feature).name = (yyvsp[0].feature).name; break;
            }
        }
#line 3553 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 129:
#line 1351 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.feature).token = TK_NAME;

            (yyval.feature).name = (yyvsp[0].text);
        }
#line 3563 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 130:
#line 1358 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            currentTimelineOrder = 0;
        }
#line 3571 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 131:
#line 1361 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                qualDef *qd;
                int nrneeded;

                /*
                 * Check that exactly one time slot in the set was requested.
                 */
                nrneeded = 0;

                for (qd = currentModule->qualifiers; qd != NULL; qd = qd->next)
                    if (qd->qtype == time_qualifier && selectedQualifier(neededQualifiers, qd))
                        ++nrneeded;

                if (nrneeded > 1)
                    yyerror("At most one of this %Timeline must be specified with the -t flag");

                currentModule->nrtimelines++;
            }
        }
#line 3597 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 134:
#line 1388 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            newQualifier(currentModule, currentModule->nrtimelines,
                    currentTimelineOrder++, TRUE, (yyvsp[0].text), time_qualifier);
        }
#line 3606 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 135:
#line 1394 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (skipStackPtr >= MAX_NESTED_IF)
                yyerror("Internal error: increase the value of MAX_NESTED_IF");

            /* Nested %Ifs are implicit logical ands. */

            if (skipStackPtr > 0)
                (yyvsp[-1].boolean) = ((yyvsp[-1].boolean) && skipStack[skipStackPtr - 1]);

            skipStack[skipStackPtr++] = (yyvsp[-1].boolean);
        }
#line 3622 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 136:
#line 1407 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.boolean) = platOrFeature((yyvsp[0].text),FALSE);
        }
#line 3630 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 137:
#line 1410 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.boolean) = platOrFeature((yyvsp[0].text),TRUE);
        }
#line 3638 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 138:
#line 1413 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.boolean) = (platOrFeature((yyvsp[0].text),FALSE) || (yyvsp[-2].boolean));
        }
#line 3646 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 139:
#line 1416 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.boolean) = (platOrFeature((yyvsp[0].text),TRUE) || (yyvsp[-3].boolean));
        }
#line 3654 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 141:
#line 1422 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.boolean) = timePeriod((yyvsp[-2].text), (yyvsp[0].text));
        }
#line 3662 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 142:
#line 1427 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (skipStackPtr-- <= 0)
                yyerror("Too many %End directives");
        }
#line 3671 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 143:
#line 1433 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            optFlag *of;

            if ((yyvsp[0].optflags).nrFlags != 0)
                deprecated("%License annotations are deprecated, use arguments instead");

            if ((yyvsp[-1].license).type == NULL)
                if ((of = getOptFlag(&(yyvsp[0].optflags), "Type", string_flag)) != NULL)
                    (yyvsp[-1].license).type = of->fvalue.sval;

            if ((yyvsp[-1].license).licensee == NULL)
                if ((of = getOptFlag(&(yyvsp[0].optflags), "Licensee", string_flag)) != NULL)
                    (yyvsp[-1].license).licensee = of->fvalue.sval;

            if ((yyvsp[-1].license).signature == NULL)
                if ((of = getOptFlag(&(yyvsp[0].optflags), "Signature", string_flag)) != NULL)
                    (yyvsp[-1].license).signature = of->fvalue.sval;

            if ((yyvsp[-1].license).timestamp == NULL)
                if ((of = getOptFlag(&(yyvsp[0].optflags), "Timestamp", string_flag)) != NULL)
                    (yyvsp[-1].license).timestamp = of->fvalue.sval;

            if ((yyvsp[-1].license).type == NULL)
                yyerror("%License must have a 'type' argument");

            if (notSkipping())
            {
                currentModule->license = sipMalloc(sizeof (licenseDef));

                currentModule->license->type = (yyvsp[-1].license).type;
                currentModule->license->licensee = (yyvsp[-1].license).licensee;
                currentModule->license->sig = (yyvsp[-1].license).signature;
                currentModule->license->timestamp = (yyvsp[-1].license).timestamp;
            }
        }
#line 3711 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 144:
#line 1470 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            (yyval.license).type = NULL;
            (yyval.license).licensee = NULL;
            (yyval.license).signature = NULL;
            (yyval.license).timestamp = NULL;
        }
#line 3724 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 145:
#line 1478 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.license).type = (yyvsp[0].text);
            (yyval.license).licensee = NULL;
            (yyval.license).signature = NULL;
            (yyval.license).timestamp = NULL;
        }
#line 3735 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 146:
#line 1484 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.license) = (yyvsp[-1].license);
        }
#line 3743 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 148:
#line 1490 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.license) = (yyvsp[-2].license);

            switch ((yyvsp[0].license).token)
            {
            case TK_TYPE: (yyval.license).type = (yyvsp[0].license).type; break;
            case TK_LICENSEE: (yyval.license).licensee = (yyvsp[0].license).licensee; break;
            case TK_SIGNATURE: (yyval.license).signature = (yyvsp[0].license).signature; break;
            case TK_TIMESTAMP: (yyval.license).timestamp = (yyvsp[0].license).timestamp; break;
            }
        }
#line 3759 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 149:
#line 1503 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.license).token = TK_NAME;

            (yyval.license).type = (yyvsp[0].text);
            (yyval.license).licensee = NULL;
            (yyval.license).signature = NULL;
            (yyval.license).timestamp = NULL;
        }
#line 3772 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 150:
#line 1511 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.license).token = TK_LICENSEE;

            (yyval.license).type = NULL;
            (yyval.license).licensee = (yyvsp[0].text);
            (yyval.license).signature = NULL;
            (yyval.license).timestamp = NULL;
        }
#line 3785 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 151:
#line 1519 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.license).token = TK_SIGNATURE;

            (yyval.license).type = NULL;
            (yyval.license).licensee = NULL;
            (yyval.license).signature = (yyvsp[0].text);
            (yyval.license).timestamp = NULL;
        }
#line 3798 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 152:
#line 1527 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.license).token = TK_TIMESTAMP;

            (yyval.license).type = NULL;
            (yyval.license).licensee = NULL;
            (yyval.license).signature = NULL;
            (yyval.license).timestamp = (yyvsp[0].text);
        }
#line 3811 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 153:
#line 1537 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                if (currentModule->defmetatype != NULL)
                    yyerror("%DefaultMetatype has already been defined for this module");

                currentModule->defmetatype = cacheName(currentSpec, (yyvsp[0].defmetatype).name);
            }
        }
#line 3825 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 154:
#line 1548 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            (yyval.defmetatype).name = (yyvsp[0].text);
        }
#line 3835 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 155:
#line 1553 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.defmetatype) = (yyvsp[-1].defmetatype);
        }
#line 3843 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 157:
#line 1559 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.defmetatype) = (yyvsp[-2].defmetatype);

            switch ((yyvsp[0].defmetatype).token)
            {
            case TK_NAME: (yyval.defmetatype).name = (yyvsp[0].defmetatype).name; break;
            }
        }
#line 3856 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 158:
#line 1569 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.defmetatype).token = TK_NAME;

            (yyval.defmetatype).name = (yyvsp[0].text);
        }
#line 3866 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 159:
#line 1576 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                if (currentModule->defsupertype != NULL)
                    yyerror("%DefaultSupertype has already been defined for this module");

                currentModule->defsupertype = cacheName(currentSpec, (yyvsp[0].defsupertype).name);
            }
        }
#line 3880 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 160:
#line 1587 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            (yyval.defsupertype).name = (yyvsp[0].text);
        }
#line 3890 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 161:
#line 1592 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.defsupertype) = (yyvsp[-1].defsupertype);
        }
#line 3898 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 163:
#line 1598 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.defsupertype) = (yyvsp[-2].defsupertype);

            switch ((yyvsp[0].defsupertype).token)
            {
            case TK_NAME: (yyval.defsupertype).name = (yyvsp[0].defsupertype).name; break;
            }
        }
#line 3911 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 164:
#line 1608 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.defsupertype).token = TK_NAME;

            (yyval.defsupertype).name = (yyvsp[0].text);
        }
#line 3921 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 165:
#line 1615 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            deprecated("%ConsolidatedModule is deprecated and will not be supported by SIP v5");

            if (notSkipping())
            {
                /* Make sure this is the first mention of a module. */
                if (currentSpec->module != currentModule)
                    yyerror("A %ConsolidatedModule cannot be %Imported");

                if (currentModule->fullname != NULL)
                    yyerror("%ConsolidatedModule must appear before any %Module or %CModule directive");

                setModuleName(currentSpec, currentModule, (yyvsp[-1].consmodule).name);
                appendCodeBlock(&currentModule->docstring, (yyvsp[0].consmodule).docstring);

                setIsConsolidated(currentModule);
            }
        }
#line 3944 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 166:
#line 1635 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            (yyval.consmodule).name = (yyvsp[0].text);
        }
#line 3954 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 167:
#line 1640 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.consmodule) = (yyvsp[-1].consmodule);
        }
#line 3962 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 169:
#line 1646 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.consmodule) = (yyvsp[-2].consmodule);

            switch ((yyvsp[0].consmodule).token)
            {
            case TK_NAME: (yyval.consmodule).name = (yyvsp[0].consmodule).name; break;
            }
        }
#line 3975 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 170:
#line 1656 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.consmodule).token = TK_NAME;

            (yyval.consmodule).name = (yyvsp[0].text);
        }
#line 3985 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 171:
#line 1663 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.consmodule).token = 0;
            (yyval.consmodule).docstring = NULL;
        }
#line 3994 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 172:
#line 1667 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.consmodule) = (yyvsp[-2].consmodule);
        }
#line 4002 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 174:
#line 1673 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.consmodule) = (yyvsp[-1].consmodule);

            switch ((yyvsp[0].consmodule).token)
            {
            case TK_DOCSTRING: (yyval.consmodule).docstring = (yyvsp[0].consmodule).docstring; break;
            }
        }
#line 4015 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 175:
#line 1683 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.consmodule).token = TK_IF;
        }
#line 4023 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 176:
#line 1686 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.consmodule).token = TK_END;
        }
#line 4031 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 177:
#line 1689 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                (yyval.consmodule).token = TK_DOCSTRING;
                (yyval.consmodule).docstring = (yyvsp[0].codeb);
            }
            else
            {
                (yyval.consmodule).token = 0;
                (yyval.consmodule).docstring = NULL;
            }
        }
#line 4048 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 178:
#line 1703 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                /* Make sure this is the first mention of a module. */
                if (currentSpec->module != currentModule)
                    yyerror("A %CompositeModule cannot be %Imported");

                if (currentModule->fullname != NULL)
                    yyerror("%CompositeModule must appear before any %Module directive");

                setModuleName(currentSpec, currentModule, (yyvsp[-1].compmodule).name);
                appendCodeBlock(&currentModule->docstring, (yyvsp[0].compmodule).docstring);

                setIsComposite(currentModule);
            }
        }
#line 4069 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 179:
#line 1721 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            (yyval.compmodule).name = (yyvsp[0].text);
        }
#line 4079 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 180:
#line 1726 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.compmodule) = (yyvsp[-1].compmodule);
        }
#line 4087 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 182:
#line 1732 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.compmodule) = (yyvsp[-2].compmodule);

            switch ((yyvsp[0].compmodule).token)
            {
            case TK_NAME: (yyval.compmodule).name = (yyvsp[0].compmodule).name; break;
            }
        }
#line 4100 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 183:
#line 1742 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.compmodule).token = TK_NAME;

            (yyval.compmodule).name = (yyvsp[0].text);
        }
#line 4110 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 184:
#line 1749 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.compmodule).token = 0;
            (yyval.compmodule).docstring = NULL;
        }
#line 4119 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 185:
#line 1753 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.compmodule) = (yyvsp[-2].compmodule);
        }
#line 4127 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 187:
#line 1759 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.compmodule) = (yyvsp[-1].compmodule);

            switch ((yyvsp[0].compmodule).token)
            {
            case TK_DOCSTRING: (yyval.compmodule).docstring = (yyvsp[0].compmodule).docstring; break;
            }
        }
#line 4140 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 188:
#line 1769 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.compmodule).token = TK_IF;
        }
#line 4148 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 189:
#line 1772 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.compmodule).token = TK_END;
        }
#line 4156 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 190:
#line 1775 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                (yyval.compmodule).token = TK_DOCSTRING;
                (yyval.compmodule).docstring = (yyvsp[0].codeb);
            }
            else
            {
                (yyval.compmodule).token = 0;
                (yyval.compmodule).docstring = NULL;
            }
        }
#line 4173 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 191:
#line 1789 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if ((yyvsp[-1].module).name == NULL)
                yyerror("%Module must have a 'name' argument");

            if (notSkipping())
                currentModule = configureModule(currentSpec, currentModule,
                        currentContext.filename, (yyvsp[-1].module).name, (yyvsp[-1].module).version,
                        (yyvsp[-1].module).c_module, (yyvsp[-1].module).kwargs, (yyvsp[-1].module).use_arg_names,
                        (yyvsp[-1].module).call_super_init, (yyvsp[-1].module).all_raise_py_exc,
                        (yyvsp[-1].module).def_error_handler, (yyvsp[0].module).docstring);
        }
#line 4189 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 192:
#line 1800 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            deprecated("%CModule is deprecated, use %Module and the 'language' argument instead");

            if (notSkipping())
                currentModule = configureModule(currentSpec, currentModule,
                        currentContext.filename, (yyvsp[-1].text), (yyvsp[0].number), TRUE, defaultKwArgs,
                        FALSE, -1, FALSE, NULL, NULL);
        }
#line 4202 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 193:
#line 1810 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {resetLexerState();}
#line 4208 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 194:
#line 1810 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if ((yyvsp[0].number) >= 0)
                deprecated("%Module version number should be specified using the 'version' argument");

            (yyval.module).c_module = FALSE;
            (yyval.module).kwargs = defaultKwArgs;
            (yyval.module).name = (yyvsp[-2].text);
            (yyval.module).use_arg_names = FALSE;
            (yyval.module).all_raise_py_exc = FALSE;
            (yyval.module).call_super_init = -1;
            (yyval.module).def_error_handler = NULL;
            (yyval.module).version = (yyvsp[0].number);
        }
#line 4226 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 195:
#line 1823 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module) = (yyvsp[-1].module);
        }
#line 4234 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 197:
#line 1829 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module) = (yyvsp[-2].module);

            switch ((yyvsp[0].module).token)
            {
            case TK_KWARGS: (yyval.module).kwargs = (yyvsp[0].module).kwargs; break;
            case TK_LANGUAGE: (yyval.module).c_module = (yyvsp[0].module).c_module; break;
            case TK_NAME: (yyval.module).name = (yyvsp[0].module).name; break;
            case TK_USEARGNAMES: (yyval.module).use_arg_names = (yyvsp[0].module).use_arg_names; break;
            case TK_ALLRAISEPYEXC: (yyval.module).all_raise_py_exc = (yyvsp[0].module).all_raise_py_exc; break;
            case TK_CALLSUPERINIT: (yyval.module).call_super_init = (yyvsp[0].module).call_super_init; break;
            case TK_DEFERRORHANDLER: (yyval.module).def_error_handler = (yyvsp[0].module).def_error_handler; break;
            case TK_VERSION: (yyval.module).version = (yyvsp[0].module).version; break;
            }
        }
#line 4254 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 198:
#line 1846 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module).token = TK_KWARGS;

            (yyval.module).c_module = FALSE;
            (yyval.module).kwargs = convertKwArgs((yyvsp[0].text));
            (yyval.module).name = NULL;
            (yyval.module).use_arg_names = FALSE;
            (yyval.module).all_raise_py_exc = FALSE;
            (yyval.module).call_super_init = -1;
            (yyval.module).def_error_handler = NULL;
            (yyval.module).version = -1;
        }
#line 4271 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 199:
#line 1858 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module).token = TK_LANGUAGE;

            if (strcmp((yyvsp[0].text), "C++") == 0)
                (yyval.module).c_module = FALSE;
            else if (strcmp((yyvsp[0].text), "C") == 0)
                (yyval.module).c_module = TRUE;
            else
                yyerror("%Module 'language' argument must be either \"C++\" or \"C\"");

            (yyval.module).kwargs = defaultKwArgs;
            (yyval.module).name = NULL;
            (yyval.module).use_arg_names = FALSE;
            (yyval.module).all_raise_py_exc = FALSE;
            (yyval.module).call_super_init = -1;
            (yyval.module).def_error_handler = NULL;
            (yyval.module).version = -1;
        }
#line 4294 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 200:
#line 1876 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module).token = TK_NAME;

            (yyval.module).c_module = FALSE;
            (yyval.module).kwargs = defaultKwArgs;
            (yyval.module).name = (yyvsp[0].text);
            (yyval.module).use_arg_names = FALSE;
            (yyval.module).all_raise_py_exc = FALSE;
            (yyval.module).call_super_init = -1;
            (yyval.module).def_error_handler = NULL;
            (yyval.module).version = -1;
        }
#line 4311 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 201:
#line 1888 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module).token = TK_USEARGNAMES;

            (yyval.module).c_module = FALSE;
            (yyval.module).kwargs = defaultKwArgs;
            (yyval.module).name = NULL;
            (yyval.module).use_arg_names = (yyvsp[0].boolean);
            (yyval.module).all_raise_py_exc = FALSE;
            (yyval.module).call_super_init = -1;
            (yyval.module).def_error_handler = NULL;
            (yyval.module).version = -1;
        }
#line 4328 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 202:
#line 1900 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module).token = TK_ALLRAISEPYEXC;

            (yyval.module).c_module = FALSE;
            (yyval.module).kwargs = defaultKwArgs;
            (yyval.module).name = NULL;
            (yyval.module).use_arg_names = FALSE;
            (yyval.module).all_raise_py_exc = (yyvsp[0].boolean);
            (yyval.module).call_super_init = -1;
            (yyval.module).def_error_handler = NULL;
            (yyval.module).version = -1;
        }
#line 4345 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 203:
#line 1912 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module).token = TK_CALLSUPERINIT;

            (yyval.module).c_module = FALSE;
            (yyval.module).kwargs = defaultKwArgs;
            (yyval.module).name = NULL;
            (yyval.module).use_arg_names = FALSE;
            (yyval.module).all_raise_py_exc = FALSE;
            (yyval.module).call_super_init = (yyvsp[0].boolean);
            (yyval.module).def_error_handler = NULL;
            (yyval.module).version = -1;
        }
#line 4362 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 204:
#line 1924 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module).token = TK_DEFERRORHANDLER;

            (yyval.module).c_module = FALSE;
            (yyval.module).kwargs = defaultKwArgs;
            (yyval.module).name = NULL;
            (yyval.module).use_arg_names = FALSE;
            (yyval.module).all_raise_py_exc = FALSE;
            (yyval.module).call_super_init = -1;
            (yyval.module).def_error_handler = (yyvsp[0].text);
            (yyval.module).version = -1;
        }
#line 4379 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 205:
#line 1936 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if ((yyvsp[0].number) < 0)
                yyerror("%Module 'version' argument cannot be negative");

            (yyval.module).token = TK_VERSION;

            (yyval.module).c_module = FALSE;
            (yyval.module).kwargs = defaultKwArgs;
            (yyval.module).name = NULL;
            (yyval.module).use_arg_names = FALSE;
            (yyval.module).all_raise_py_exc = FALSE;
            (yyval.module).call_super_init = -1;
            (yyval.module).def_error_handler = NULL;
            (yyval.module).version = (yyvsp[0].number);
        }
#line 4399 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 206:
#line 1953 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module).token = 0;
            (yyval.module).docstring = NULL;
        }
#line 4408 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 207:
#line 1957 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module) = (yyvsp[-2].module);
        }
#line 4416 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 209:
#line 1963 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module) = (yyvsp[-1].module);

            switch ((yyvsp[0].module).token)
            {
            case TK_DOCSTRING: (yyval.module).docstring = (yyvsp[0].module).docstring; break;
            }
        }
#line 4429 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 210:
#line 1973 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module).token = TK_IF;
        }
#line 4437 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 211:
#line 1976 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module).token = TK_END;
        }
#line 4445 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 212:
#line 1979 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.module).token = TK_AUTOPYNAME;
        }
#line 4453 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 213:
#line 1982 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                (yyval.module).token = TK_DOCSTRING;
                (yyval.module).docstring = (yyvsp[0].codeb);
            }
            else
            {
                (yyval.module).token = 0;
                (yyval.module).docstring = NULL;
            }
        }
#line 4470 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 215:
#line 1997 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /*
             * The grammar design is a bit broken and this is the easiest way
             * to allow periods in names.
             */

            char *cp;

            for (cp = (yyvsp[0].text); *cp != '\0'; ++cp)
                if (*cp != '.' && *cp != '_' && !isalnum(*cp))
                    yyerror("Invalid character in name");

            (yyval.text) = (yyvsp[0].text);
        }
#line 4489 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 216:
#line 2013 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.number) = -1;
        }
#line 4497 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 218:
#line 2019 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if ((yyvsp[0].include).name == NULL)
                yyerror("%Include must have a 'name' argument");

            if (notSkipping())
                parseFile(NULL, (yyvsp[0].include).name, NULL, (yyvsp[0].include).optional);
        }
#line 4509 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 219:
#line 2028 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            (yyval.include).name = (yyvsp[0].text);
            (yyval.include).optional = FALSE;
        }
#line 4520 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 220:
#line 2034 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.include) = (yyvsp[-1].include);
        }
#line 4528 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 222:
#line 2040 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.include) = (yyvsp[-2].include);

            switch ((yyvsp[0].include).token)
            {
            case TK_NAME: (yyval.include).name = (yyvsp[0].include).name; break;
            case TK_OPTIONAL: (yyval.include).optional = (yyvsp[0].include).optional; break;
            }
        }
#line 4542 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 223:
#line 2051 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.include).token = TK_NAME;

            (yyval.include).name = (yyvsp[0].text);
            (yyval.include).optional = FALSE;
        }
#line 4553 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 224:
#line 2057 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.include).token = TK_OPTIONAL;

            (yyval.include).name = NULL;
            (yyval.include).optional = (yyvsp[0].boolean);
        }
#line 4564 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 225:
#line 2065 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            deprecated("%OptionalInclude is deprecated, use %Include and the 'optional' argument instead");

            if (notSkipping())
                parseFile(NULL, (yyvsp[0].text), NULL, TRUE);
        }
#line 4575 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 226:
#line 2073 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                newImport((yyvsp[0].import).name);
        }
#line 4584 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 227:
#line 2079 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            (yyval.import).name = (yyvsp[0].text);
        }
#line 4594 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 228:
#line 2084 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.import) = (yyvsp[-1].import);
        }
#line 4602 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 230:
#line 2090 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.import) = (yyvsp[-2].import);

            switch ((yyvsp[0].import).token)
            {
            case TK_NAME: (yyval.import).name = (yyvsp[0].import).name; break;
            }
        }
#line 4615 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 231:
#line 2100 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.import).token = TK_NAME;

            (yyval.import).name = (yyvsp[0].text);
        }
#line 4625 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 232:
#line 2107 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = NULL;
        }
#line 4633 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 233:
#line 2110 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4641 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 234:
#line 2115 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = NULL;
        }
#line 4649 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 235:
#line 2118 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4657 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 236:
#line 2123 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = NULL;
        }
#line 4665 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 237:
#line 2126 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4673 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 238:
#line 2131 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentModule->copying, (yyvsp[0].codeb));
        }
#line 4682 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 239:
#line 2137 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentSpec->exphdrcode, (yyvsp[0].codeb));
        }
#line 4691 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 240:
#line 2143 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentModule->hdrcode, (yyvsp[0].codeb));
        }
#line 4700 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 241:
#line 2149 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4708 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 242:
#line 2154 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4716 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 243:
#line 2159 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4724 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 244:
#line 2164 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4732 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 245:
#line 2169 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4740 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 246:
#line 2174 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4748 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 247:
#line 2179 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4756 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 248:
#line 2184 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4764 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 249:
#line 2189 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4772 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 250:
#line 2194 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4780 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 251:
#line 2199 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4788 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 252:
#line 2204 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4796 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 253:
#line 2209 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentModule->cppcode, (yyvsp[0].codeb));
        }
#line 4805 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 254:
#line 2215 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4813 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 255:
#line 2220 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentModule->preinitcode, (yyvsp[0].codeb));
        }
#line 4822 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 256:
#line 2226 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentModule->initcode, (yyvsp[0].codeb));
        }
#line 4831 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 257:
#line 2232 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentModule->postinitcode, (yyvsp[0].codeb));
        }
#line 4840 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 258:
#line 2238 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentModule->unitcode, (yyvsp[0].codeb));
        }
#line 4849 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 259:
#line 2244 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentModule->unitpostinccode, (yyvsp[0].codeb));
        }
#line 4858 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 260:
#line 2250 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* Deprecated. */
        }
#line 4866 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 261:
#line 2255 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping() && !inMainModule())
                appendCodeBlock(&currentSpec->exptypehintcode, (yyvsp[0].codeb));
        }
#line 4875 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 262:
#line 2261 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentModule->typehintcode, (yyvsp[0].codeb));
        }
#line 4884 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 263:
#line 2267 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 4892 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 264:
#line 2272 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping() && inMainModule())
                appendCodeBlock(&currentSpec->docs, (yyvsp[0].codeb));
        }
#line 4901 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 265:
#line 2278 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentSpec->docs, (yyvsp[0].codeb));
        }
#line 4910 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 266:
#line 2284 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                addAutoPyName(currentModule, (yyvsp[0].autopyname).remove_leading);
        }
#line 4919 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 267:
#line 2290 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.autopyname) = (yyvsp[-1].autopyname);
        }
#line 4927 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 269:
#line 2296 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.autopyname) = (yyvsp[-2].autopyname);

            switch ((yyvsp[0].autopyname).token)
            {
            case TK_REMOVELEADING: (yyval.autopyname).remove_leading = (yyvsp[0].autopyname).remove_leading; break;
            }
        }
#line 4940 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 270:
#line 2306 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.autopyname).token = TK_REMOVELEADING;

            (yyval.autopyname).remove_leading = (yyvsp[0].text);
        }
#line 4950 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 271:
#line 2313 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);

            /* Format the docstring. */
            if ((yyvsp[-1].docstring).format == deindented)
            {
                const char *cp;
                char *dp;
                int min_indent, indent, skipping;

                /* Find the common indent. */
                min_indent = -1;
                indent = 0;
                skipping = FALSE;

                for (cp = (yyval.codeb)->frag; *cp != '\0'; ++cp)
                {
                    if (skipping)
                    {
                        /*
                         * We have handled the indent and are just looking for
                         * the end of the line.
                         */
                        if (*cp == '\n')
                            skipping = FALSE;
                    }
                    else
                    {
                        if (*cp == ' ')
                        {
                            ++indent;
                        }
                        else if (*cp != '\n')
                        {
                            if (min_indent < 0 || min_indent > indent)
                                min_indent = indent;

                            /* Ignore the remaining characters of the line. */
                            skipping = TRUE;
                        }
                    }
                }

                /* In case the last line doesn't have a trailing newline. */
                if (min_indent < 0 || min_indent > indent)
                    min_indent = indent;

                /*
                 * Go through the text again removing the common indentation.
                 */
                cp = dp = (yyval.codeb)->frag;

                while (*cp != '\0')
                {
                    const char *start = cp;
                    int non_blank = FALSE;

                    /* Find the end of the line. */
                    while (*cp != '\n' && *cp != '\0')
                        if (*cp++ != ' ')
                            non_blank = TRUE;

                    /* Find where we are copying from. */
                    if (non_blank)
                    {
                        start += min_indent;

                        while (*start != '\n' && *start != '\0')
                            *dp++ = *start++;
                    }

                    if (*cp == '\n')
                        *dp++ = *cp++;
                }

                *dp = '\0';
            }
        }
#line 5033 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 272:
#line 2393 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.docstring).format = currentModule->defdocstring;
        }
#line 5041 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 273:
#line 2396 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            (yyval.docstring).format = convertFormat((yyvsp[0].text));
        }
#line 5051 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 274:
#line 2401 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.docstring) = (yyvsp[-1].docstring);
        }
#line 5059 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 276:
#line 2407 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.docstring) = (yyvsp[-2].docstring);

            switch ((yyvsp[0].docstring).token)
            {
            case TK_FORMAT: (yyval.docstring).format = (yyvsp[0].docstring).format; break;
            }
        }
#line 5072 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 277:
#line 2417 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.docstring).token = TK_FORMAT;

            (yyval.docstring).format = convertFormat((yyvsp[0].text));
        }
#line 5082 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 278:
#line 2424 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = NULL;
        }
#line 5090 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 280:
#line 2430 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if ((yyvsp[-1].extract).id == NULL)
                yyerror("%Extract must have an 'id' argument");

            if (notSkipping())
                addExtractPart(currentSpec, (yyvsp[-1].extract).id, (yyvsp[-1].extract).order, (yyvsp[0].codeb));
        }
#line 5102 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 281:
#line 2439 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            resetLexerState();

            (yyval.extract).id = (yyvsp[0].text);
            (yyval.extract).order = -1;
        }
#line 5113 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 282:
#line 2445 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.extract) = (yyvsp[-1].extract);
        }
#line 5121 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 284:
#line 2451 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.extract) = (yyvsp[-2].extract);

            switch ((yyvsp[0].extract).token)
            {
            case TK_ID: (yyval.extract).id = (yyvsp[0].extract).id; break;
            case TK_ORDER: (yyval.extract).order = (yyvsp[0].extract).order; break;
            }
        }
#line 5135 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 285:
#line 2462 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.extract).token = TK_ID;

            (yyval.extract).id = (yyvsp[0].text);
            (yyval.extract).order = -1;
        }
#line 5146 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 286:
#line 2468 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.extract).token = TK_ORDER;

            if ((yyvsp[0].number) < 0)
                yyerror("The 'order' of an %Extract directive must not be negative");

            (yyval.extract).id = NULL;
            (yyval.extract).order = (yyvsp[0].number);
        }
#line 5160 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 287:
#line 2479 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* Deprecated. */
        }
#line 5168 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 290:
#line 2488 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[-1].codeb);

            append(&(yyval.codeb)->frag, (yyvsp[0].codeb)->frag);

            free((yyvsp[0].codeb)->frag);
            free((yyvsp[0].codeb));
        }
#line 5181 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 291:
#line 2498 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                const char *annos[] = {
                    "NoScope",
                    "NoTypeHint",
                    "PyName",
                    NULL
                };

                checkAnnos(&(yyvsp[0].optflags), annos);

                if (sectionFlags != 0 && (sectionFlags & ~(SECT_IS_PUBLIC | SECT_IS_PROT)) != 0)
                    yyerror("Class enums must be in the public or protected sections");

                currentEnum = newEnum(currentSpec, currentModule,
                        currentMappedType, (yyvsp[-1].text), &(yyvsp[0].optflags), sectionFlags);
            }
        }
#line 5205 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 293:
#line 2519 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.text) = NULL;
        }
#line 5213 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 294:
#line 2522 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.text) = (yyvsp[0].text);
        }
#line 5221 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 295:
#line 2527 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.text) = NULL;
        }
#line 5229 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 296:
#line 2530 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.text) = (yyvsp[0].text);
        }
#line 5237 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 303:
#line 2545 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                const char *annos[] = {
                    "NoTypeHint",
                    "PyName",
                    NULL
                };

                enumMemberDef *emd, **tail;

                checkAnnos(&(yyvsp[-1].optflags), annos);

                /* Note that we don't use the assigned value. */
                emd = sipMalloc(sizeof (enumMemberDef));

                emd->pyname = cacheName(currentSpec,
                        getPythonName(currentModule, &(yyvsp[-1].optflags), (yyvsp[-3].text)));
                emd->cname = (yyvsp[-3].text);
                emd->no_typehint = getNoTypeHint(&(yyvsp[-1].optflags));
                emd->ed = currentEnum;
                emd->next = NULL;

                checkAttributes(currentSpec, currentModule, emd->ed->ecd,
                        emd->ed->emtd, emd->pyname->text, FALSE);

                /* Append to preserve the order. */
                for (tail = &currentEnum->members; *tail != NULL; tail = &(*tail)->next)
                    ;

                *tail = emd;

                if (inMainModule())
                    setIsUsedName(emd->pyname);
            }
        }
#line 5278 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 308:
#line 2591 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.valp) = NULL;
        }
#line 5286 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 309:
#line 2594 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.valp) = (yyvsp[0].valp);
        }
#line 5294 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 311:
#line 2600 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            valueDef *vd;
 
            if ((yyvsp[-2].valp) -> vtype == string_value || (yyvsp[0].valp) -> vtype == string_value)
                yyerror("Invalid binary operator for string");
 
            /* Find the last value in the existing expression. */
 
            for (vd = (yyvsp[-2].valp); vd -> next != NULL; vd = vd -> next)
                ;
 
            vd -> vbinop = (yyvsp[-1].qchar);
            vd -> next = (yyvsp[0].valp);

            (yyval.valp) = (yyvsp[-2].valp);
        }
#line 5315 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 312:
#line 2618 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.qchar) = '-';
        }
#line 5323 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 313:
#line 2621 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.qchar) = '+';
        }
#line 5331 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 314:
#line 2624 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.qchar) = '*';
        }
#line 5339 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 315:
#line 2627 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.qchar) = '/';
        }
#line 5347 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 316:
#line 2630 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.qchar) = '&';
        }
#line 5355 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 317:
#line 2633 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.qchar) = '|';
        }
#line 5363 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 318:
#line 2638 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.qchar) = '\0';
        }
#line 5371 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 319:
#line 2641 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.qchar) = '!';
        }
#line 5379 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 320:
#line 2644 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.qchar) = '~';
        }
#line 5387 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 321:
#line 2647 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.qchar) = '-';
        }
#line 5395 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 322:
#line 2650 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.qchar) = '+';
        }
#line 5403 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 323:
#line 2653 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.qchar) = '*';
        }
#line 5411 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 324:
#line 2656 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.qchar) = '&';
        }
#line 5419 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 325:
#line 2661 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if ((yyvsp[-1].qchar) != '\0' && (yyvsp[0].value).vtype == string_value)
                yyerror("Invalid unary operator for string");
 
            /* Convert the value to a simple expression on the heap. */
            (yyval.valp) = sipMalloc(sizeof (valueDef));
 
            *(yyval.valp) = (yyvsp[0].value);
            (yyval.valp)->vunop = (yyvsp[-1].qchar);
            (yyval.valp)->vbinop = '\0';
            (yyval.valp)->cast = (yyvsp[-2].scpvalp);
            (yyval.valp)->next = NULL;
        }
#line 5437 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 326:
#line 2676 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.scpvalp) = NULL;
        }
#line 5445 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 327:
#line 2679 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.scpvalp) = (yyvsp[-1].scpvalp);
        }
#line 5453 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 329:
#line 2685 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (currentSpec -> genc)
                yyerror("Scoped names are not allowed in a C module");

            appendScopedName(&(yyvsp[-2].scpvalp),(yyvsp[0].scpvalp));
        }
#line 5464 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 330:
#line 2693 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.scpvalp) = text2scopePart((yyvsp[0].text));
        }
#line 5472 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 331:
#line 2698 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.boolean) = TRUE;
        }
#line 5480 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 332:
#line 2701 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.boolean) = FALSE;
        }
#line 5488 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 333:
#line 2706 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /*
             * We let the C++ compiler decide if the value is a valid one - no
             * point in building a full C++ parser here.
             */

            (yyval.value).vtype = scoped_value;
            (yyval.value).u.vscp = (yyvsp[0].scpvalp);
        }
#line 5502 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 334:
#line 2715 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            fcallDef *fcd;

            fcd = sipMalloc(sizeof (fcallDef));
            *fcd = (yyvsp[-1].fcall);
            fcd -> type = (yyvsp[-3].memArg);

            (yyval.value).vtype = fcall_value;
            (yyval.value).u.fcd = fcd;
        }
#line 5517 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 335:
#line 2725 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.value).vtype = real_value;
            (yyval.value).u.vreal = (yyvsp[0].real);
        }
#line 5526 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 336:
#line 2729 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.value).vtype = numeric_value;
            (yyval.value).u.vnum = (yyvsp[0].number);
        }
#line 5535 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 337:
#line 2733 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.value).vtype = numeric_value;
            (yyval.value).u.vnum = (yyvsp[0].boolean);
        }
#line 5544 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 338:
#line 2737 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.value).vtype = numeric_value;
            (yyval.value).u.vnum = 0;
        }
#line 5553 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 339:
#line 2741 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.value).vtype = string_value;
            (yyval.value).u.vstr = (yyvsp[0].text);
        }
#line 5562 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 340:
#line 2745 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.value).vtype = qchar_value;
            (yyval.value).u.vqchar = (yyvsp[0].qchar);
        }
#line 5571 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 341:
#line 2751 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* No values. */

            (yyval.fcall).nrArgs = 0;
        }
#line 5581 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 342:
#line 2756 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* The single or first expression. */

            (yyval.fcall).args[0] = (yyvsp[0].valp);
            (yyval.fcall).nrArgs = 1;
        }
#line 5592 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 343:
#line 2762 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* Check that it wasn't ...(,expression...). */

            if ((yyval.fcall).nrArgs == 0)
                yyerror("First argument to function call is missing");

            /* Check there is room. */

            if ((yyvsp[-2].fcall).nrArgs == MAX_NR_ARGS)
                yyerror("Internal error - increase the value of MAX_NR_ARGS");

            (yyval.fcall) = (yyvsp[-2].fcall);

            (yyval.fcall).args[(yyval.fcall).nrArgs] = (yyvsp[0].valp);
            (yyval.fcall).nrArgs++;
        }
#line 5613 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 344:
#line 2780 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                const char *annos[] = {
                    "Capsule",
                    "DocType",
                    "Encoding",
                    "NoTypeName",
                    "PyInt",
                    "PyName",
                    "TypeHint",
                    "TypeHintIn",
                    "TypeHintOut",
                    NULL
                };

                checkAnnos(&(yyvsp[-1].optflags), annos);

                applyTypeFlags(currentModule, &(yyvsp[-3].memArg), &(yyvsp[-1].optflags));
                newTypedef(currentSpec, currentModule, (yyvsp[-2].text), &(yyvsp[-3].memArg), &(yyvsp[-1].optflags));
            }
        }
#line 5640 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 345:
#line 2802 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                const char *annos[] = {
                    "DocType",
                    "Encoding",
                    "NoTypeName",
                    "PyInt",
                    "PyName",
                    "TypeHint",
                    "TypeHintIn",
                    "TypeHintOut",
                    NULL
                };

                signatureDef *sig;
                argDef ftype;

                checkAnnos(&(yyvsp[-1].optflags), annos);

                applyTypeFlags(currentModule, &(yyvsp[-9].memArg), &(yyvsp[-1].optflags));

                memset(&ftype, 0, sizeof (argDef));

                /* Create the full signature on the heap. */
                sig = sipMalloc(sizeof (signatureDef));
                *sig = (yyvsp[-3].signature);
                sig->result = (yyvsp[-9].memArg);

                /* Create the full type. */
                ftype.atype = function_type;
                ftype.nrderefs = 1;
                ftype.u.sa = sig;

                newTypedef(currentSpec, currentModule, (yyvsp[-6].text), &ftype, &(yyvsp[-1].optflags));
            }
        }
#line 5682 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 346:
#line 2841 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (currentSpec -> genc && (yyvsp[0].scpvalp)->next != NULL)
                yyerror("Namespaces not allowed in a C module");

            if (notSkipping())
                currentSupers = NULL;
        }
#line 5694 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 347:
#line 2847 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                const char *annos[] = {
                    "Abstract",
                    "AllowNone",
                    "API",
                    "DelayDtor",
                    "Deprecated",
                    "ExportDerived",
                    "External",
                    "FileExtension",
                    "Metatype",
                    "Mixin",
                    "NoDefaultCtors",
                    "NoTypeHint",
                    "PyName",
                    "PyQtFlags",
                    "PyQtInterface",
                    "PyQtNoQMetaObject",
                    "Supertype",
                    "TypeHint",
                    "TypeHintIn",
                    "TypeHintOut",
                    "TypeHintValue",
                    "VirtualErrorHandler",
                    NULL
                };

                checkAnnos(&(yyvsp[0].optflags), annos);

                if (currentSpec->genc && currentSupers != NULL)
                    yyerror("Super-classes not allowed in a C module struct");

                defineClass((yyvsp[-3].scpvalp), currentSupers, &(yyvsp[0].optflags));
                sectionFlags = SECT_IS_PUBLIC;
            }
        }
#line 5737 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 348:
#line 2884 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                completeClass((yyvsp[-6].scpvalp), &(yyvsp[-3].optflags), (yyvsp[-1].boolean));
        }
#line 5746 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 349:
#line 2890 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {currentIsTemplate = TRUE;}
#line 5752 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 350:
#line 2890 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (currentSpec->genc)
                yyerror("Class templates not allowed in a C module");

            if (notSkipping())
            {
                classTmplDef *tcd;

                /*
                 * Make sure there is room for the extra class name argument.
                 */
                if ((yyvsp[-2].signature).nrArgs == MAX_NR_ARGS)
                    yyerror("Internal error - increase the value of MAX_NR_ARGS");

                tcd = sipMalloc(sizeof (classTmplDef));
                tcd->sig = (yyvsp[-2].signature);
                tcd->cd = (yyvsp[0].klass);
                tcd->next = currentSpec->classtemplates;

                currentSpec->classtemplates = tcd;
            }

            currentIsTemplate = FALSE;
        }
#line 5781 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 351:
#line 2916 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.signature) = (yyvsp[-1].signature);
        }
#line 5789 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 352:
#line 2921 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (currentSpec->genc)
                yyerror("Class definition not allowed in a C module");

            if (notSkipping())
                currentSupers = NULL;
        }
#line 5801 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 353:
#line 2927 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                const char *annos[] = {
                    "Abstract",
                    "AllowNone",
                    "API",
                    "DelayDtor",
                    "Deprecated",
                    "ExportDerived",
                    "External",
                    "FileExtension",
                    "Metatype",
                    "Mixin",
                    "NoDefaultCtors",
                    "PyName",
                    "PyQtFlags",
                    "PyQtInterface",
                    "PyQtNoQMetaObject",
                    "Supertype",
                    "TypeHint",
                    "TypeHintIn",
                    "TypeHintOut",
                    "TypeHintValue",
                    "VirtualErrorHandler",
                    NULL
                };

                checkAnnos(&(yyvsp[0].optflags), annos);

                defineClass((yyvsp[-3].scpvalp), currentSupers, &(yyvsp[0].optflags));
                sectionFlags = SECT_IS_PRIVATE;
            }
        }
#line 5840 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 354:
#line 2960 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                (yyval.klass) = completeClass((yyvsp[-6].scpvalp), &(yyvsp[-3].optflags), (yyvsp[-1].boolean));
        }
#line 5849 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 359:
#line 2974 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping() && (yyvsp[-1].token) == TK_PUBLIC)
            {
                argDef ad;
                classDef *super;
                scopedNameDef *snd = (yyvsp[0].scpvalp);

                /*
                 * This is a hack to allow typedef'ed classes to be used before
                 * we have resolved the typedef definitions.  Unlike elsewhere,
                 * we require that the typedef is defined before being used.
                 */
                for (;;)
                {
                    ad.atype = no_type;
                    ad.argflags = 0;
                    ad.nrderefs = 0;
                    ad.original_type = NULL;

                    searchTypedefs(currentSpec, snd, &ad);

                    if (ad.atype != defined_type)
                        break;

                    if (ad.nrderefs != 0 || isConstArg(&ad) || isReference(&ad))
                        break;

                    snd = ad.u.snd;
                }

                if (ad.atype != no_type)
                    yyerror("Super-class list contains an invalid type");

                /*
                 * Note that passing NULL as the API is a bug.  Instead we
                 * should pass the API of the sub-class being defined,
                 * otherwise we cannot create sub-classes of versioned classes.
                 */
                super = findClass(currentSpec, class_iface, NULL, snd);
                appendToClassList(&currentSupers, super);
            }
        }
#line 5896 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 360:
#line 3018 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
        (yyval.token) = TK_PUBLIC;
        }
#line 5904 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 361:
#line 3021 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
        (yyval.token) = TK_PUBLIC;
        }
#line 5912 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 362:
#line 3024 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
        (yyval.token) = TK_PROTECTED;
        }
#line 5920 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 363:
#line 3027 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
        (yyval.token) = TK_PRIVATE;
        }
#line 5928 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 364:
#line 3032 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.boolean) = FALSE;
        }
#line 5936 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 365:
#line 3035 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.boolean) = TRUE;
        }
#line 5944 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 377:
#line 3053 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentScope()->docstring, (yyvsp[0].codeb));
        }
#line 5953 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 378:
#line 3057 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentScope()->cppcode, (yyvsp[0].codeb));
        }
#line 5962 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 379:
#line 3061 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
                appendCodeBlock(&currentScope()->iff->hdrcode, (yyvsp[0].codeb));
        }
#line 5971 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 380:
#line 3065 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->travcode != NULL)
                    yyerror("%GCTraverseCode already given for class");

                appendCodeBlock(&scope->travcode, (yyvsp[0].codeb));
            }
        }
#line 5987 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 381:
#line 3076 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->clearcode != NULL)
                    yyerror("%GCClearCode already given for class");

                appendCodeBlock(&scope->clearcode, (yyvsp[0].codeb));
            }
        }
#line 6003 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 382:
#line 3087 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->getbufcode != NULL)
                    yyerror("%BIGetBufferCode already given for class");

                appendCodeBlock(&scope->getbufcode, (yyvsp[0].codeb));
            }
        }
#line 6019 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 383:
#line 3098 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->releasebufcode != NULL)
                    yyerror("%BIReleaseBufferCode already given for class");

                appendCodeBlock(&scope->releasebufcode, (yyvsp[0].codeb));
            }
        }
#line 6035 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 384:
#line 3109 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->readbufcode != NULL)
                    yyerror("%BIGetReadBufferCode already given for class");

                appendCodeBlock(&scope->readbufcode, (yyvsp[0].codeb));
            }
        }
#line 6051 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 385:
#line 3120 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->writebufcode != NULL)
                    yyerror("%BIGetWriteBufferCode already given for class");

                appendCodeBlock(&scope->writebufcode, (yyvsp[0].codeb));
            }
        }
#line 6067 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 386:
#line 3131 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->segcountcode != NULL)
                    yyerror("%BIGetSegCountCode already given for class");

                appendCodeBlock(&scope->segcountcode, (yyvsp[0].codeb));
            }
        }
#line 6083 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 387:
#line 3142 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->charbufcode != NULL)
                    yyerror("%BIGetCharBufferCode already given for class");

                appendCodeBlock(&scope->charbufcode, (yyvsp[0].codeb));
            }
        }
#line 6099 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 388:
#line 3153 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->instancecode != NULL)
                    yyerror("%InstanceCode already given for class");

                appendCodeBlock(&scope->instancecode, (yyvsp[0].codeb));
            }
        }
#line 6115 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 389:
#line 3164 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->picklecode != NULL)
                    yyerror("%PickleCode already given for class");

                appendCodeBlock(&scope->picklecode, (yyvsp[0].codeb));
            }
        }
#line 6131 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 390:
#line 3175 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->finalcode != NULL)
                    yyerror("%FinalisationCode already given for class");

                appendCodeBlock(&scope->finalcode, (yyvsp[0].codeb));
            }
        }
#line 6147 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 391:
#line 3186 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->typehintcode != NULL)
                    yyerror("%TypeHintCode already given for class");

                appendCodeBlock(&scope->typehintcode, (yyvsp[0].codeb));
            }
        }
#line 6163 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 395:
#line 3200 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->convtosubcode != NULL)
                    yyerror("Class has more than one %ConvertToSubClassCode directive");

                appendCodeBlock(&scope->convtosubcode, (yyvsp[0].codeb));
            }
        }
#line 6179 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 396:
#line 3211 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->convtocode != NULL)
                    yyerror("Class has more than one %ConvertToTypeCode directive");

                appendCodeBlock(&scope->convtocode, (yyvsp[0].codeb));
            }
        }
#line 6195 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 397:
#line 3222 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *scope = currentScope();

                if (scope->convfromcode != NULL)
                    yyerror("Class has more than one %ConvertFromTypeCode directive");

                appendCodeBlock(&scope->convfromcode, (yyvsp[0].codeb));
            }
        }
#line 6211 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 398:
#line 3233 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (currentSpec -> genc)
                yyerror("public section not allowed in a C module");

            if (notSkipping())
                sectionFlags = SECT_IS_PUBLIC | (yyvsp[-1].number);
        }
#line 6223 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 399:
#line 3240 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (currentSpec -> genc)
                yyerror("protected section not allowed in a C module");

            if (notSkipping())
                sectionFlags = SECT_IS_PROT | (yyvsp[-1].number);
        }
#line 6235 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 400:
#line 3247 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (currentSpec -> genc)
                yyerror("private section not allowed in a C module");

            if (notSkipping())
                sectionFlags = SECT_IS_PRIVATE | (yyvsp[-1].number);
        }
#line 6247 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 401:
#line 3254 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (currentSpec -> genc)
                yyerror("signals section not allowed in a C module");

            if (notSkipping())
                sectionFlags = SECT_IS_SIGNAL;
        }
#line 6259 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 402:
#line 3263 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if ((yyvsp[-1].property).name == NULL)
                yyerror("A %Property directive must have a 'name' argument");

            if ((yyvsp[-1].property).get == NULL)
                yyerror("A %Property directive must have a 'get' argument");

            if (notSkipping())
                addProperty(currentSpec, currentModule, currentScope(),
                        (yyvsp[-1].property).name, (yyvsp[-1].property).get, (yyvsp[-1].property).set, (yyvsp[0].property).docstring);
        }
#line 6275 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 403:
#line 3276 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.property) = (yyvsp[-1].property);
        }
#line 6283 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 405:
#line 3282 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.property) = (yyvsp[-2].property);

            switch ((yyvsp[0].property).token)
            {
            case TK_GET: (yyval.property).get = (yyvsp[0].property).get; break;
            case TK_NAME: (yyval.property).name = (yyvsp[0].property).name; break;
            case TK_SET: (yyval.property).set = (yyvsp[0].property).set; break;
            }
        }
#line 6298 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 406:
#line 3294 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.property).token = TK_GET;

            (yyval.property).get = (yyvsp[0].text);
            (yyval.property).name = NULL;
            (yyval.property).set = NULL;
        }
#line 6310 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 407:
#line 3301 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.property).token = TK_NAME;

            (yyval.property).get = NULL;
            (yyval.property).name = (yyvsp[0].text);
            (yyval.property).set = NULL;
        }
#line 6322 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 408:
#line 3308 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.property).token = TK_SET;

            (yyval.property).get = NULL;
            (yyval.property).name = NULL;
            (yyval.property).set = (yyvsp[0].text);
        }
#line 6334 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 409:
#line 3317 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.property).token = 0;
            (yyval.property).docstring = NULL;
        }
#line 6343 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 410:
#line 3321 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.property) = (yyvsp[-2].property);
        }
#line 6351 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 412:
#line 3327 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.property) = (yyvsp[-1].property);

            switch ((yyvsp[0].property).token)
            {
            case TK_DOCSTRING: (yyval.property).docstring = (yyvsp[0].property).docstring; break;
            }
        }
#line 6364 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 413:
#line 3337 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.property).token = TK_IF;
        }
#line 6372 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 414:
#line 3340 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.property).token = TK_END;
        }
#line 6380 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 415:
#line 3343 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                (yyval.property).token = TK_DOCSTRING;
                (yyval.property).docstring = (yyvsp[0].codeb);
            }
            else
            {
                (yyval.property).token = 0;
                (yyval.property).docstring = NULL;
            }
        }
#line 6397 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 418:
#line 3361 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.number) = 0;
        }
#line 6405 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 419:
#line 3364 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.number) = SECT_IS_SLOT;
        }
#line 6413 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 420:
#line 3369 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* Note that we allow non-virtual dtors in C modules. */

            if (notSkipping())
            {
                const char *annos[] = {
                    "HoldGIL",
                    "ReleaseGIL",
                    NULL
                };

                classDef *cd = currentScope();

                checkAnnos(&(yyvsp[-3].optflags), annos);

                if (strcmp(classBaseName(cd),(yyvsp[-8].text)) != 0)
                    yyerror("Destructor doesn't have the same name as its class");

                if (isDtor(cd))
                    yyerror("Destructor has already been defined");

                if (currentSpec -> genc && (yyvsp[-1].codeb) == NULL)
                    yyerror("Destructor in C modules must include %MethodCode");

                appendCodeBlock(&cd->dealloccode, (yyvsp[-1].codeb));
                appendCodeBlock(&cd->dtorcode, (yyvsp[0].codeb));
                cd -> dtorexceptions = (yyvsp[-5].throwlist);

                /*
                 * Note that we don't apply the protected/public hack to dtors
                 * as it (I think) may change the behaviour of the wrapped API.
                 */
                cd->classflags |= sectionFlags;

                if ((yyvsp[-4].number))
                {
                    if (!(yyvsp[-10].number))
                        yyerror("Abstract destructor must be virtual");

                    setIsAbstractClass(cd);
                }

                /*
                 * The class has a shadow if we have a virtual dtor or some
                 * dtor code.
                 */
                if ((yyvsp[-10].number) || (yyvsp[0].codeb) != NULL)
                {
                    if (currentSpec -> genc)
                        yyerror("Virtual destructor or %VirtualCatcherCode not allowed in a C module");

                    setHasShadow(cd);
                }

                if (getReleaseGIL(&(yyvsp[-3].optflags)))
                    setIsReleaseGILDtor(cd);
                else if (getHoldGIL(&(yyvsp[-3].optflags)))
                    setIsHoldGILDtor(cd);
            }
        }
#line 6478 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 421:
#line 3431 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {currentCtorIsExplicit = TRUE;}
#line 6484 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 424:
#line 3435 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* Note that we allow ctors in C modules. */

            if (notSkipping())
            {
                const char *annos[] = {
                    "API",
                    "Default",
                    "Deprecated",
                    "HoldGIL",
                    "KeywordArgs",
                    "NoDerived",
                    "NoRaisesPyException",
                    "NoTypeHint",
                    "PostHook",
                    "PreHook",
                    "RaisesPyException",
                    "ReleaseGIL",
                    "Transfer",
                    NULL
                };

                checkAnnos(&(yyvsp[-4].optflags), annos);

                if (currentSpec -> genc)
                {
                    if ((yyvsp[0].codeb) == NULL && (yyvsp[-7].signature).nrArgs != 0)
                        yyerror("Constructors with arguments in C modules must include %MethodCode");

                    if (currentCtorIsExplicit)
                        yyerror("Explicit constructors not allowed in a C module");
                }

                if ((sectionFlags & (SECT_IS_PUBLIC | SECT_IS_PROT | SECT_IS_PRIVATE)) == 0)
                    yyerror("Constructor must be in the public, private or protected sections");

                newCtor(currentModule, (yyvsp[-9].text), sectionFlags, &(yyvsp[-7].signature), &(yyvsp[-4].optflags), (yyvsp[0].codeb), (yyvsp[-5].throwlist), (yyvsp[-3].optsignature),
                        currentCtorIsExplicit, (yyvsp[-1].codeb));
            }

            free((yyvsp[-9].text));

            currentCtorIsExplicit = FALSE;
        }
#line 6533 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 425:
#line 3481 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.optsignature) = NULL;
        }
#line 6541 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 426:
#line 3484 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            parsingCSignature = TRUE;
        }
#line 6549 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 427:
#line 3486 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.optsignature) = sipMalloc(sizeof (signatureDef));

            *(yyval.optsignature) = (yyvsp[-2].signature);

            parsingCSignature = FALSE;
        }
#line 6561 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 428:
#line 3495 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.optsignature) = NULL;
        }
#line 6569 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 429:
#line 3498 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            parsingCSignature = TRUE;
        }
#line 6577 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 430:
#line 3500 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.optsignature) = sipMalloc(sizeof (signatureDef));

            *(yyval.optsignature) = (yyvsp[-2].signature);
            (yyval.optsignature)->result = (yyvsp[-4].memArg);

            parsingCSignature = FALSE;
        }
#line 6590 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 431:
#line 3510 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.number) = FALSE;
        }
#line 6598 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 432:
#line 3513 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.number) = TRUE;
        }
#line 6606 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 433:
#line 3518 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                applyTypeFlags(currentModule, &(yyvsp[-14].memArg), &(yyvsp[-6].optflags));

                (yyvsp[-11].signature).result = (yyvsp[-14].memArg);

                newFunction(currentSpec, currentModule, currentScope(), NULL,
                        sectionFlags, currentIsStatic, currentIsSignal,
                        currentIsSlot, currentOverIsVirt, (yyvsp[-13].text), &(yyvsp[-11].signature), (yyvsp[-9].number), (yyvsp[-7].number), &(yyvsp[-6].optflags),
                        (yyvsp[-2].codeb), (yyvsp[-1].codeb), (yyvsp[0].codeb), (yyvsp[-8].throwlist), (yyvsp[-5].optsignature), (yyvsp[-3].codeb));
            }

            currentIsStatic = FALSE;
            currentIsSignal = FALSE;
            currentIsSlot = FALSE;
            currentOverIsVirt = FALSE;
        }
#line 6629 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 434:
#line 3536 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /*
             * It looks like an assignment operator (though we don't bother to
             * check the types) so make sure it is private.
             */
            if (notSkipping())
            {
                classDef *cd = currentScope();

                if (cd == NULL || !(sectionFlags & SECT_IS_PRIVATE))
                    yyerror("Assignment operators may only be defined as private");

                setCannotAssign(cd);
            }

            currentIsStatic = FALSE;
            currentIsSignal = FALSE;
            currentIsSlot = FALSE;
            currentOverIsVirt = FALSE;
        }
#line 6654 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 435:
#line 3556 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                classDef *cd = currentScope();

                /*
                 * If the scope is a namespace then make sure the operator is
                 * handled as a global.
                 */
                if (cd != NULL && cd->iff->type == namespace_iface)
                    cd = NULL;

                applyTypeFlags(currentModule, &(yyvsp[-14].memArg), &(yyvsp[-5].optflags));

                /* Handle the unary '+' and '-' operators. */
                if ((cd != NULL && (yyvsp[-10].signature).nrArgs == 0) || (cd == NULL && (yyvsp[-10].signature).nrArgs == 1))
                {
                    if (strcmp((yyvsp[-12].text), "__add__") == 0)
                        (yyvsp[-12].text) = "__pos__";
                    else if (strcmp((yyvsp[-12].text), "__sub__") == 0)
                        (yyvsp[-12].text) = "__neg__";
                }

                (yyvsp[-10].signature).result = (yyvsp[-14].memArg);

                newFunction(currentSpec, currentModule, cd, NULL,
                        sectionFlags, currentIsStatic, currentIsSignal,
                        currentIsSlot, currentOverIsVirt, (yyvsp[-12].text), &(yyvsp[-10].signature), (yyvsp[-8].number), (yyvsp[-6].number),
                        &(yyvsp[-5].optflags), (yyvsp[-2].codeb), (yyvsp[-1].codeb), (yyvsp[0].codeb), (yyvsp[-7].throwlist), (yyvsp[-4].optsignature), NULL);
            }

            currentIsStatic = FALSE;
            currentIsSignal = FALSE;
            currentIsSlot = FALSE;
            currentOverIsVirt = FALSE;
        }
#line 6695 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 436:
#line 3592 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                char *sname;
                classDef *scope = currentScope();

                if (scope == NULL || (yyvsp[-10].signature).nrArgs != 0)
                    yyerror("Operator casts must be specified in a class and have no arguments");

                applyTypeFlags(currentModule, &(yyvsp[-12].memArg), &(yyvsp[-5].optflags));

                switch ((yyvsp[-12].memArg).atype)
                {
                case defined_type:
                    sname = NULL;
                    break;

                case bool_type:
                case cbool_type:
                case byte_type:
                case sbyte_type:
                case ubyte_type:
                case short_type:
                case ushort_type:
                case int_type:
                case cint_type:
                case uint_type:
                    sname = "__int__";
                    break;

                case long_type:
                case ulong_type:
                case longlong_type:
                case ulonglong_type:
                    sname = "__long__";
                    break;

                case float_type:
                case cfloat_type:
                case double_type:
                case cdouble_type:
                    sname = "__float__";
                    break;

                default:
                    yyerror("Unsupported operator cast");
                }

                if (sname != NULL)
                {
                    (yyvsp[-10].signature).result = (yyvsp[-12].memArg);

                    newFunction(currentSpec, currentModule, scope, NULL,
                            sectionFlags, currentIsStatic, currentIsSignal,
                            currentIsSlot, currentOverIsVirt, sname, &(yyvsp[-10].signature), (yyvsp[-8].number),
                            (yyvsp[-6].number), &(yyvsp[-5].optflags), (yyvsp[-2].codeb), (yyvsp[-1].codeb), (yyvsp[0].codeb), (yyvsp[-7].throwlist), (yyvsp[-4].optsignature), NULL);
                }
                else
                {
                    argList *al;

                    /* Check it doesn't already exist. */
                    for (al = scope->casts; al != NULL; al = al->next)
                        if (compareScopedNames((yyvsp[-12].memArg).u.snd, al->arg.u.snd) == 0)
                            yyerror("This operator cast has already been specified in this class");

                    al = sipMalloc(sizeof (argList));
                    al->arg = (yyvsp[-12].memArg);
                    al->next = scope->casts;

                    scope->casts = al;
                }
            }

            currentIsStatic = FALSE;
            currentIsSignal = FALSE;
            currentIsSlot = FALSE;
            currentOverIsVirt = FALSE;
        }
#line 6779 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 437:
#line 3673 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__add__";}
#line 6785 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 438:
#line 3674 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__sub__";}
#line 6791 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 439:
#line 3675 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__mul__";}
#line 6797 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 440:
#line 3676 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__div__";}
#line 6803 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 441:
#line 3677 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__mod__";}
#line 6809 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 442:
#line 3678 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__and__";}
#line 6815 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 443:
#line 3679 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__or__";}
#line 6821 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 444:
#line 3680 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__xor__";}
#line 6827 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 445:
#line 3681 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__lshift__";}
#line 6833 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 446:
#line 3682 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__rshift__";}
#line 6839 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 447:
#line 3683 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__iadd__";}
#line 6845 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 448:
#line 3684 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__isub__";}
#line 6851 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 449:
#line 3685 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__imul__";}
#line 6857 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 450:
#line 3686 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__idiv__";}
#line 6863 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 451:
#line 3687 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__imod__";}
#line 6869 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 452:
#line 3688 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__iand__";}
#line 6875 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 453:
#line 3689 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__ior__";}
#line 6881 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 454:
#line 3690 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__ixor__";}
#line 6887 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 455:
#line 3691 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__ilshift__";}
#line 6893 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 456:
#line 3692 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__irshift__";}
#line 6899 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 457:
#line 3693 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__invert__";}
#line 6905 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 458:
#line 3694 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__call__";}
#line 6911 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 459:
#line 3695 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__getitem__";}
#line 6917 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 460:
#line 3696 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__lt__";}
#line 6923 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 461:
#line 3697 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__le__";}
#line 6929 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 462:
#line 3698 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__eq__";}
#line 6935 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 463:
#line 3699 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__ne__";}
#line 6941 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 464:
#line 3700 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__gt__";}
#line 6947 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 465:
#line 3701 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {(yyval.text) = "__ge__";}
#line 6953 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 466:
#line 3704 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.number) = FALSE;
        }
#line 6961 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 467:
#line 3707 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.number) = TRUE;
        }
#line 6969 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 468:
#line 3712 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.number) = 0;
        }
#line 6977 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 469:
#line 3715 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if ((yyvsp[0].number) != 0)
                yyerror("Abstract virtual function '= 0' expected");

            (yyval.number) = TRUE;
        }
#line 6988 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 470:
#line 3723 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.optflags).nrFlags = 0;
        }
#line 6996 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 471:
#line 3726 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.optflags) = (yyvsp[-1].optflags);
        }
#line 7004 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 472:
#line 3732 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.optflags).flags[0] = (yyvsp[0].flag);
            (yyval.optflags).nrFlags = 1;
        }
#line 7013 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 473:
#line 3736 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* Check there is room. */

            if ((yyvsp[-2].optflags).nrFlags == MAX_NR_FLAGS)
                yyerror("Too many optional flags");

            (yyval.optflags) = (yyvsp[-2].optflags);

            (yyval.optflags).flags[(yyval.optflags).nrFlags++] = (yyvsp[0].flag);
        }
#line 7028 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 474:
#line 3748 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.flag).ftype = bool_flag;
            (yyval.flag).fname = (yyvsp[0].text);
        }
#line 7037 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 475:
#line 3752 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.flag) = (yyvsp[0].flag);
            (yyval.flag).fname = (yyvsp[-2].text);
        }
#line 7046 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 476:
#line 3758 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.flag).ftype = (strchr((yyvsp[0].text), '.') != NULL) ? dotted_name_flag : name_flag;
            (yyval.flag).fvalue.sval = (yyvsp[0].text);
        }
#line 7055 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 477:
#line 3762 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            apiVersionRangeDef *avd;
            int from, to;

            (yyval.flag).ftype = api_range_flag;

            /* Check that the API is known. */
            if ((avd = findAPI(currentSpec, (yyvsp[-4].text))) == NULL)
                yyerror("unknown API name in API annotation");

            if (inMainModule())
                setIsUsedName(avd->api_name);

            /* Unbounded values are represented by 0. */
            if ((from = (yyvsp[-2].number)) < 0)
                from = 0;

            if ((to = (yyvsp[0].number)) < 0)
                to = 0;

            (yyval.flag).fvalue.aval = convertAPIRange(currentModule, avd->api_name,
                    from, to);
        }
#line 7083 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 478:
#line 3785 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.flag).ftype = string_flag;
            (yyval.flag).fvalue.sval = convertFeaturedString((yyvsp[0].text));
        }
#line 7092 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 479:
#line 3789 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.flag).ftype = integer_flag;
            (yyval.flag).fvalue.ival = (yyvsp[0].number);
        }
#line 7101 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 480:
#line 3795 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = NULL;
        }
#line 7109 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 481:
#line 3798 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 7117 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 482:
#line 3803 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = NULL;
        }
#line 7125 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 483:
#line 3806 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 7133 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 484:
#line 3811 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = NULL;
        }
#line 7141 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 485:
#line 3814 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.codeb) = (yyvsp[0].codeb);
        }
#line 7149 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 486:
#line 3819 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            int a, nrrxcon, nrrxdis, nrslotcon, nrslotdis, nrarray, nrarraysize;

            nrrxcon = nrrxdis = nrslotcon = nrslotdis = nrarray = nrarraysize = 0;

            for (a = 0; a < (yyvsp[0].signature).nrArgs; ++a)
            {
                argDef *ad = &(yyvsp[0].signature).args[a];

                switch (ad -> atype)
                {
                case rxcon_type:
                    ++nrrxcon;
                    break;

                case rxdis_type:
                    ++nrrxdis;
                    break;

                case slotcon_type:
                    ++nrslotcon;
                    break;

                case slotdis_type:
                    ++nrslotdis;
                    break;

                /* Suppress a compiler warning. */
                default:
                    ;
                }

                if (isArray(ad))
                    ++nrarray;

                if (isArraySize(ad))
                    ++nrarraysize;
            }

            if (nrrxcon != nrslotcon || nrrxcon > 1)
                yyerror("SIP_RXOBJ_CON and SIP_SLOT_CON must both be given and at most once");

            if (nrrxdis != nrslotdis || nrrxdis > 1)
                yyerror("SIP_RXOBJ_DIS and SIP_SLOT_DIS must both be given and at most once");

            if (nrarray != nrarraysize || nrarray > 1)
                yyerror("/Array/ and /ArraySize/ must both be given and at most once");

            (yyval.signature) = (yyvsp[0].signature);
        }
#line 7204 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 487:
#line 3871 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* No arguments. */

            (yyval.signature).nrArgs = 0;
        }
#line 7214 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 488:
#line 3876 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* The single or first argument. */

            (yyval.signature).args[0] = (yyvsp[0].memArg);
            (yyval.signature).nrArgs = 1;
        }
#line 7225 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 489:
#line 3882 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* Check that it wasn't ...(,arg...). */
            if ((yyvsp[-2].signature).nrArgs == 0)
                yyerror("First argument of the list is missing");

            /*
             * If this argument has no default value, then the
             * previous one mustn't either.
             */
            if ((yyvsp[0].memArg).defval == NULL && (yyvsp[-2].signature).args[(yyvsp[-2].signature).nrArgs - 1].defval != NULL)
                yyerror("Compulsory argument given after optional argument");

            /* Check there is room. */
            if ((yyvsp[-2].signature).nrArgs == MAX_NR_ARGS)
                yyerror("Internal error - increase the value of MAX_NR_ARGS");

            (yyval.signature) = (yyvsp[-2].signature);

            (yyval.signature).args[(yyval.signature).nrArgs] = (yyvsp[0].memArg);
            (yyval.signature).nrArgs++;
        }
#line 7251 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 490:
#line 3905 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            deprecated("SIP_SIGNAL is deprecated\n");
            checkNoAnnos(&(yyvsp[-1].optflags), "SIP_SIGNAL has no annotations");

            (yyval.memArg).atype = signal_type;
            (yyval.memArg).argflags = ARG_IS_CONST;
            (yyval.memArg).nrderefs = 0;
            (yyval.memArg).name = cacheName(currentSpec, (yyvsp[-2].text));
            (yyval.memArg).defval = (yyvsp[0].valp);

            currentSpec -> sigslots = TRUE;
        }
#line 7268 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 491:
#line 3917 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            deprecated("SIP_SLOT is deprecated\n");
            checkNoAnnos(&(yyvsp[-1].optflags), "SIP_SLOT has no annotations");

            (yyval.memArg).atype = slot_type;
            (yyval.memArg).argflags = ARG_IS_CONST;
            (yyval.memArg).nrderefs = 0;
            (yyval.memArg).name = cacheName(currentSpec, (yyvsp[-2].text));
            (yyval.memArg).defval = (yyvsp[0].valp);

            currentSpec -> sigslots = TRUE;
        }
#line 7285 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 492:
#line 3929 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            deprecated("SIP_ANYSLOT is deprecated\n");
            checkNoAnnos(&(yyvsp[-1].optflags), "SIP_ANYSLOT has no annotations");

            (yyval.memArg).atype = anyslot_type;
            (yyval.memArg).argflags = ARG_IS_CONST;
            (yyval.memArg).nrderefs = 0;
            (yyval.memArg).name = cacheName(currentSpec, (yyvsp[-2].text));
            (yyval.memArg).defval = (yyvsp[0].valp);

            currentSpec -> sigslots = TRUE;
        }
#line 7302 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 493:
#line 3941 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            const char *annos[] = {
                "SingleShot",
                NULL
            };

            deprecated("SIP_RXOBJ_CON is deprecated\n");
            checkAnnos(&(yyvsp[0].optflags), annos);

            (yyval.memArg).atype = rxcon_type;
            (yyval.memArg).argflags = 0;
            (yyval.memArg).nrderefs = 0;
            (yyval.memArg).name = cacheName(currentSpec, (yyvsp[-1].text));

            if (getOptFlag(&(yyvsp[0].optflags), "SingleShot", bool_flag) != NULL)
                (yyval.memArg).argflags |= ARG_SINGLE_SHOT;

            currentSpec -> sigslots = TRUE;
        }
#line 7326 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 494:
#line 3960 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            deprecated("SIP_RXOBJ_DIS is deprecated\n");
            checkNoAnnos(&(yyvsp[0].optflags), "SIP_RXOBJ_DIS has no annotations");

            (yyval.memArg).atype = rxdis_type;
            (yyval.memArg).argflags = 0;
            (yyval.memArg).nrderefs = 0;
            (yyval.memArg).name = cacheName(currentSpec, (yyvsp[-1].text));

            currentSpec -> sigslots = TRUE;
        }
#line 7342 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 495:
#line 3971 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            deprecated("SIP_SLOT_CON is deprecated\n");
            checkNoAnnos(&(yyvsp[0].optflags), "SIP_SLOT_CON has no annotations");

            (yyval.memArg).atype = slotcon_type;
            (yyval.memArg).argflags = ARG_IS_CONST;
            (yyval.memArg).nrderefs = 0;
            (yyval.memArg).name = cacheName(currentSpec, (yyvsp[-1].text));

            memset(&(yyvsp[-3].signature).result, 0, sizeof (argDef));
            (yyvsp[-3].signature).result.atype = void_type;

            (yyval.memArg).u.sa = sipMalloc(sizeof (signatureDef));
            *(yyval.memArg).u.sa = (yyvsp[-3].signature);

            currentSpec -> sigslots = TRUE;
        }
#line 7364 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 496:
#line 3988 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            deprecated("SIP_SLOT_DIS is deprecated\n");
            checkNoAnnos(&(yyvsp[0].optflags), "SIP_SLOT_DIS has no annotations");

            (yyval.memArg).atype = slotdis_type;
            (yyval.memArg).argflags = ARG_IS_CONST;
            (yyval.memArg).nrderefs = 0;
            (yyval.memArg).name = cacheName(currentSpec, (yyvsp[-1].text));

            memset(&(yyvsp[-3].signature).result, 0, sizeof (argDef));
            (yyvsp[-3].signature).result.atype = void_type;

            (yyval.memArg).u.sa = sipMalloc(sizeof (signatureDef));
            *(yyval.memArg).u.sa = (yyvsp[-3].signature);

            currentSpec -> sigslots = TRUE;
        }
#line 7386 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 497:
#line 4005 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            deprecated("SIP_QOBJECT is deprecated\n");
            checkNoAnnos(&(yyvsp[0].optflags), "SIP_QOBJECT has no annotations");

            (yyval.memArg).atype = qobject_type;
            (yyval.memArg).argflags = 0;
            (yyval.memArg).nrderefs = 0;
            (yyval.memArg).name = cacheName(currentSpec, (yyvsp[-1].text));
        }
#line 7400 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 498:
#line 4014 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.memArg) = (yyvsp[-1].memArg);
            (yyval.memArg).defval = (yyvsp[0].valp);
        }
#line 7409 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 499:
#line 4021 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {currentIsSignal = TRUE;}
#line 7415 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 501:
#line 4022 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {currentIsSlot = TRUE;}
#line 7421 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 504:
#line 4027 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {currentIsStatic = TRUE;}
#line 7427 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 509:
#line 4037 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {currentOverIsVirt = TRUE;}
#line 7433 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 512:
#line 4041 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                const char *annos[] = {
                    "DocType",
                    "Encoding",
                    "NoSetter",
                    "NoTypeHint",
                    "PyInt",
                    "PyName",
                    "TypeHint",
                    NULL
                };

                checkAnnos(&(yyvsp[-5].optflags), annos);

                if ((yyvsp[-2].codeb) != NULL)
                {
                    if ((yyvsp[-4].variable).access_code != NULL)
                        yyerror("%AccessCode already defined");

                    (yyvsp[-4].variable).access_code = (yyvsp[-2].codeb);

                    deprecated("%AccessCode should be used as a sub-directive");
                }

                if ((yyvsp[-1].codeb) != NULL)
                {
                    if ((yyvsp[-4].variable).get_code != NULL)
                        yyerror("%GetCode already defined");

                    (yyvsp[-4].variable).get_code = (yyvsp[-1].codeb);

                    deprecated("%GetCode should be used as a sub-directive");
                }

                if ((yyvsp[0].codeb) != NULL)
                {
                    if ((yyvsp[-4].variable).set_code != NULL)
                        yyerror("%SetCode already defined");

                    (yyvsp[-4].variable).set_code = (yyvsp[0].codeb);

                    deprecated("%SetCode should be used as a sub-directive");
                }

                newVar(currentSpec, currentModule, (yyvsp[-6].text), currentIsStatic, &(yyvsp[-7].memArg),
                        &(yyvsp[-5].optflags), (yyvsp[-4].variable).access_code, (yyvsp[-4].variable).get_code, (yyvsp[-4].variable).set_code,
                        sectionFlags);
            }

            currentIsStatic = FALSE;
        }
#line 7491 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 513:
#line 4096 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.variable).token = 0;
            (yyval.variable).access_code = NULL;
            (yyval.variable).get_code = NULL;
            (yyval.variable).set_code = NULL;
        }
#line 7502 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 514:
#line 4102 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.variable) = (yyvsp[-1].variable);
        }
#line 7510 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 516:
#line 4108 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.variable) = (yyvsp[-1].variable);

            switch ((yyvsp[0].variable).token)
            {
            case TK_ACCESSCODE: (yyval.variable).access_code = (yyvsp[0].variable).access_code; break;
            case TK_GETCODE: (yyval.variable).get_code = (yyvsp[0].variable).get_code; break;
            case TK_SETCODE: (yyval.variable).set_code = (yyvsp[0].variable).set_code; break;
            }
        }
#line 7525 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 517:
#line 4120 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.variable).token = TK_IF;
        }
#line 7533 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 518:
#line 4123 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.variable).token = TK_END;
        }
#line 7541 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 519:
#line 4126 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                (yyval.variable).token = TK_ACCESSCODE;
                (yyval.variable).access_code = (yyvsp[0].codeb);
            }
            else
            {
                (yyval.variable).token = 0;
                (yyval.variable).access_code = NULL;
            }

            (yyval.variable).get_code = NULL;
            (yyval.variable).set_code = NULL;
        }
#line 7561 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 520:
#line 4141 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                (yyval.variable).token = TK_GETCODE;
                (yyval.variable).get_code = (yyvsp[0].codeb);
            }
            else
            {
                (yyval.variable).token = 0;
                (yyval.variable).get_code = NULL;
            }

            (yyval.variable).access_code = NULL;
            (yyval.variable).set_code = NULL;
        }
#line 7581 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 521:
#line 4156 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (notSkipping())
            {
                (yyval.variable).token = TK_SETCODE;
                (yyval.variable).set_code = (yyvsp[0].codeb);
            }
            else
            {
                (yyval.variable).token = 0;
                (yyval.variable).set_code = NULL;
            }

            (yyval.variable).access_code = NULL;
            (yyval.variable).get_code = NULL;
        }
#line 7601 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 522:
#line 4173 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.memArg) = (yyvsp[-2].memArg);
            add_derefs(&(yyval.memArg), &(yyvsp[-1].memArg));
            (yyval.memArg).argflags |= ARG_IS_CONST | (yyvsp[0].number);
        }
#line 7611 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 523:
#line 4178 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.memArg) = (yyvsp[-2].memArg);
            add_derefs(&(yyval.memArg), &(yyvsp[-1].memArg));
            (yyval.memArg).argflags |= (yyvsp[0].number);

            /* PyObject * is a synonym for SIP_PYOBJECT. */
            if ((yyvsp[-2].memArg).atype == defined_type && strcmp((yyvsp[-2].memArg).u.snd->name, "PyObject") == 0 && (yyvsp[-2].memArg).u.snd->next == NULL && (yyvsp[-1].memArg).nrderefs == 1 && (yyvsp[0].number) == 0)
            {
                (yyval.memArg).atype = pyobject_type;
                (yyval.memArg).nrderefs = 0;
            }
        }
#line 7628 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 524:
#line 4192 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            const char *annos[] = {
                "AllowNone",
                "Array",
                "ArraySize",
                "Constrained",
                "DisallowNone",
                "DocType",
                "DocValue",
                "Encoding",
                "GetWrapper",
                "In",
                "KeepReference",
                "NoCopy",
                "Out",
                "PyInt",
                "ResultSize",
                "Transfer",
                "TransferBack",
                "TransferThis",
                "TypeHint",
                "TypeHintIn",
                "TypeHintOut",
                "TypeHintValue",
                NULL
            };

            checkAnnos(&(yyvsp[0].optflags), annos);

            (yyval.memArg) = (yyvsp[-2].memArg);
            (yyval.memArg).name = cacheName(currentSpec, (yyvsp[-1].text));

            handleKeepReference(&(yyvsp[0].optflags), &(yyval.memArg), currentModule);

            if (getAllowNone(&(yyvsp[0].optflags)))
                (yyval.memArg).argflags |= ARG_ALLOW_NONE;

            if (getDisallowNone(&(yyvsp[0].optflags)))
                (yyval.memArg).argflags |= ARG_DISALLOW_NONE;

            if (getOptFlag(&(yyvsp[0].optflags),"GetWrapper",bool_flag) != NULL)
                (yyval.memArg).argflags |= ARG_GET_WRAPPER;

            if (getOptFlag(&(yyvsp[0].optflags),"Array",bool_flag) != NULL)
                (yyval.memArg).argflags |= ARG_ARRAY;

            if (getOptFlag(&(yyvsp[0].optflags),"ArraySize",bool_flag) != NULL)
                (yyval.memArg).argflags |= ARG_ARRAY_SIZE;

            if (getTransfer(&(yyvsp[0].optflags)))
                (yyval.memArg).argflags |= ARG_XFERRED;

            if (getOptFlag(&(yyvsp[0].optflags),"TransferThis",bool_flag) != NULL)
                (yyval.memArg).argflags |= ARG_THIS_XFERRED;

            if (getOptFlag(&(yyvsp[0].optflags),"TransferBack",bool_flag) != NULL)
                (yyval.memArg).argflags |= ARG_XFERRED_BACK;

            if (getOptFlag(&(yyvsp[0].optflags),"In",bool_flag) != NULL)
                (yyval.memArg).argflags |= ARG_IN;

            if (getOptFlag(&(yyvsp[0].optflags),"Out",bool_flag) != NULL)
                (yyval.memArg).argflags |= ARG_OUT;

            if (getOptFlag(&(yyvsp[0].optflags), "ResultSize", bool_flag) != NULL)
                (yyval.memArg).argflags |= ARG_RESULT_SIZE;

            if (getOptFlag(&(yyvsp[0].optflags), "NoCopy", bool_flag) != NULL)
                (yyval.memArg).argflags |= ARG_NO_COPY;

            if (getOptFlag(&(yyvsp[0].optflags),"Constrained",bool_flag) != NULL)
            {
                (yyval.memArg).argflags |= ARG_CONSTRAINED;

                switch ((yyval.memArg).atype)
                {
                case bool_type:
                    (yyval.memArg).atype = cbool_type;
                    break;

                case int_type:
                    (yyval.memArg).atype = cint_type;
                    break;

                case float_type:
                    (yyval.memArg).atype = cfloat_type;
                    break;

                case double_type:
                    (yyval.memArg).atype = cdouble_type;
                    break;

                /* Suppress a compiler warning. */
                default:
                    ;
                }
            }

            applyTypeFlags(currentModule, &(yyval.memArg), &(yyvsp[0].optflags));
            (yyval.memArg).typehint_value = getTypeHintValue(&(yyvsp[0].optflags));
        }
#line 7734 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 525:
#line 4295 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.number) = 0;
        }
#line 7742 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 526:
#line 4298 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (currentSpec -> genc)
                yyerror("References not allowed in a C module");

            (yyval.number) = ARG_IS_REF;
        }
#line 7753 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 527:
#line 4306 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.memArg).nrderefs = 0;
        }
#line 7761 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 528:
#line 4309 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            add_new_deref(&(yyval.memArg), &(yyvsp[-2].memArg), TRUE);
        }
#line 7769 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 529:
#line 4312 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            add_new_deref(&(yyval.memArg), &(yyvsp[-1].memArg), FALSE);
        }
#line 7777 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 530:
#line 4317 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = defined_type;
            (yyval.memArg).u.snd = (yyvsp[0].scpvalp);

            /* Try and resolve typedefs as early as possible. */
            resolveAnyTypedef(currentSpec, &(yyval.memArg));
        }
#line 7790 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 531:
#line 4325 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            templateDef *td;

            td = sipMalloc(sizeof(templateDef));
            td->fqname = (yyvsp[-3].scpvalp);
            td->types = (yyvsp[-1].signature);

            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = template_type;
            (yyval.memArg).u.td = td;
        }
#line 7806 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 532:
#line 4336 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));

            /* In a C module all structures must be defined. */
            if (currentSpec -> genc)
            {
                (yyval.memArg).atype = defined_type;
                (yyval.memArg).u.snd = (yyvsp[0].scpvalp);
            }
            else
            {
                (yyval.memArg).atype = struct_type;
                (yyval.memArg).u.sname = (yyvsp[0].scpvalp);
            }
        }
#line 7826 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 533:
#line 4351 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = ushort_type;
        }
#line 7835 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 534:
#line 4355 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = short_type;
        }
#line 7844 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 535:
#line 4359 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = uint_type;
        }
#line 7853 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 536:
#line 4363 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = uint_type;
        }
#line 7862 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 537:
#line 4367 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = int_type;
        }
#line 7871 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 538:
#line 4371 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = long_type;
        }
#line 7880 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 539:
#line 4375 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = ulong_type;
        }
#line 7889 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 540:
#line 4379 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = longlong_type;
        }
#line 7898 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 541:
#line 4383 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = ulonglong_type;
        }
#line 7907 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 542:
#line 4387 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = float_type;
        }
#line 7916 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 543:
#line 4391 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = double_type;
        }
#line 7925 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 544:
#line 4395 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = bool_type;
        }
#line 7934 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 545:
#line 4399 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = sstring_type;
        }
#line 7943 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 546:
#line 4403 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = ustring_type;
        }
#line 7952 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 547:
#line 4407 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = string_type;
        }
#line 7961 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 548:
#line 4411 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = wstring_type;
        }
#line 7970 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 549:
#line 4415 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = void_type;
        }
#line 7979 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 550:
#line 4419 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = pyobject_type;
        }
#line 7988 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 551:
#line 4423 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = pytuple_type;
        }
#line 7997 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 552:
#line 4427 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = pylist_type;
        }
#line 8006 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 553:
#line 4431 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = pydict_type;
        }
#line 8015 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 554:
#line 4435 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = pycallable_type;
        }
#line 8024 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 555:
#line 4439 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = pyslice_type;
        }
#line 8033 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 556:
#line 4443 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = pytype_type;
        }
#line 8042 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 557:
#line 4447 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = pybuffer_type;
        }
#line 8051 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 558:
#line 4451 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = ssize_type;
        }
#line 8060 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 559:
#line 4455 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            memset(&(yyval.memArg), 0, sizeof (argDef));
            (yyval.memArg).atype = ellipsis_type;
        }
#line 8069 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 560:
#line 4461 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* The single or first type. */

            (yyval.signature).args[0] = (yyvsp[0].memArg);
            (yyval.signature).nrArgs = 1;
        }
#line 8080 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 561:
#line 4467 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* Check there is nothing after an ellipsis. */
            if ((yyvsp[-2].signature).args[(yyvsp[-2].signature).nrArgs - 1].atype == ellipsis_type)
                yyerror("An ellipsis must be at the end of the argument list");

            /* Check there is room. */
            if ((yyvsp[-2].signature).nrArgs == MAX_NR_ARGS)
                yyerror("Internal error - increase the value of MAX_NR_ARGS");

            (yyval.signature) = (yyvsp[-2].signature);

            (yyval.signature).args[(yyval.signature).nrArgs] = (yyvsp[0].memArg);
            (yyval.signature).nrArgs++;
        }
#line 8099 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 562:
#line 4483 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            (yyval.throwlist) = NULL;
        }
#line 8107 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 563:
#line 4486 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            if (currentSpec->genc)
                yyerror("Exceptions not allowed in a C module");

            (yyval.throwlist) = (yyvsp[-1].throwlist);
        }
#line 8118 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 564:
#line 4494 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* Empty list so use a blank. */

            (yyval.throwlist) = sipMalloc(sizeof (throwArgs));
            (yyval.throwlist) -> nrArgs = 0;
        }
#line 8129 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 565:
#line 4500 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* The only or first exception. */

            (yyval.throwlist) = sipMalloc(sizeof (throwArgs));
            (yyval.throwlist) -> nrArgs = 1;
            (yyval.throwlist) -> args[0] = findException(currentSpec, (yyvsp[0].scpvalp), FALSE);
        }
#line 8141 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;

  case 566:
#line 4507 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1646  */
    {
            /* Check that it wasn't ...(,arg...). */

            if ((yyvsp[-2].throwlist) -> nrArgs == 0)
                yyerror("First exception of throw specifier is missing");

            /* Check there is room. */

            if ((yyvsp[-2].throwlist) -> nrArgs == MAX_NR_ARGS)
                yyerror("Internal error - increase the value of MAX_NR_ARGS");

            (yyval.throwlist) = (yyvsp[-2].throwlist);
            (yyval.throwlist) -> args[(yyval.throwlist) -> nrArgs++] = findException(currentSpec, (yyvsp[0].scpvalp), FALSE);
        }
#line 8160 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
    break;


#line 8164 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/parser.c" /* yacc.c:1646  */
      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = (char *) YYSTACK_ALLOC (yymsg_alloc);
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYTERROR;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#if !defined yyoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  return yyresult;
}
#line 4523 "/home/bob/hg/sip/sip-4.18-snapshot-a4f8a7810cc3/sipgen/metasrc/parser.y" /* yacc.c:1906  */



/*
 * Parse the specification.
 */
void parse(sipSpec *spec, FILE *fp, char *filename, stringList *tsl,
        stringList *bsl, stringList *xfl, KwArgs kwArgs, int protHack)
{
    classTmplDef *tcd;

    /* Initialise the spec. */
 
    memset(spec, 0, sizeof (sipSpec));
    spec->genc = -1;

    currentSpec = spec;
    backstops = bsl;
    neededQualifiers = tsl;
    excludedQualifiers = xfl;
    currentModule = NULL;
    currentMappedType = NULL;
    currentOverIsVirt = FALSE;
    currentCtorIsExplicit = FALSE;
    currentIsStatic = FALSE;
    currentIsSignal = FALSE;
    currentIsSlot = FALSE;
    currentIsTemplate = FALSE;
    previousFile = NULL;
    skipStackPtr = 0;
    currentScopeIdx = 0;
    sectionFlags = 0;
    defaultKwArgs = kwArgs;
    makeProtPublic = protHack;

    newModule(fp, filename);
    spec->module = currentModule;

    yyparse();

    handleEOF();
    handleEOM();

    /*
     * Go through each template class and remove it from the list of classes.
     */
    for (tcd = spec->classtemplates; tcd != NULL; tcd = tcd->next)
    {
        classDef **cdp;

        for (cdp = &spec->classes; *cdp != NULL; cdp = &(*cdp)->next)
            if (*cdp == tcd->cd)
            {
                ifaceFileDef **ifdp;

                /* Remove the interface file as well. */
                for (ifdp = &spec->ifacefiles; *ifdp != NULL; ifdp = &(*ifdp)->next)
                    if (*ifdp == tcd->cd->iff)
                    {
                        *ifdp = (*ifdp)->next;
                        break;
                    }

                *cdp = (*cdp)->next;
                break;
            }
    }
}


/*
 * Tell the parser that a complete file has now been read.
 */
void parserEOF(const char *name, parserContext *pc)
{
    previousFile = sipStrdup(name);
    currentContext = *pc;
}


/*
 * Append a class definition to a class list if it doesn't already appear.
 * Append is needed specifically for the list of super-classes because the
 * order is important to Python.
 */
void appendToClassList(classList **clp,classDef *cd)
{
    classList *new;

    /* Find the end of the list. */

    while (*clp != NULL)
    {
        if ((*clp) -> cd == cd)
            return;

        clp = &(*clp) -> next;
    }

    new = sipMalloc(sizeof (classList));

    new -> cd = cd;
    new -> next = NULL;

    *clp = new;
}


/*
 * Create a new module for the current specification and make it current.
 */
static void newModule(FILE *fp, const char *filename)
{
    moduleDef *mod;

    parseFile(fp, filename, currentModule, FALSE);

    mod = allocModule();
    mod->file = filename;

    if (currentModule != NULL)
        mod->defexception = currentModule->defexception;

    currentModule = mod;
}


/*
 * Allocate and initialise the memory for a new module.
 */
static moduleDef *allocModule()
{
    moduleDef *newmod, **tailp;

    newmod = sipMalloc(sizeof (moduleDef));

    newmod->version = -1;
    newmod->defdocstring = raw;
    newmod->encoding = no_type;
    newmod->nrvirthandlers = -1;
    newmod->next_key = -1;

    /*
     * The consolidated module support needs these to be in order that they
     * appeared.
     */
    for (tailp = &currentSpec->modules; *tailp != NULL; tailp = &(*tailp)->next)
        ;

    *tailp = newmod;

    return newmod;
}


/*
 * Switch to parsing a new file.
 */
static void parseFile(FILE *fp, const char *name, moduleDef *prevmod,
        int optional)
{
    parserContext pc;

    pc.filename = name;
    pc.ifdepth = skipStackPtr;
    pc.prevmod = prevmod;

    if (setInputFile(fp, &pc, optional))
        currentContext = pc;
}


/*
 * Find an interface file, or create a new one.
 */
ifaceFileDef *findIfaceFile(sipSpec *pt, moduleDef *mod, scopedNameDef *fqname,
        ifaceFileType iftype, apiVersionRangeDef *api_range, argDef *ad)
{
    ifaceFileDef *iff, *first_alt = NULL;

    /* See if the name is already used. */

    for (iff = pt->ifacefiles; iff != NULL; iff = iff->next)
    {
        if (compareScopedNames(iff->fqcname, fqname) != 0)
            continue;

        /*
         * If they are both versioned then assume the user knows what they are
         * doing.
         */
        if (iff->api_range != NULL && api_range != NULL && iff->module == mod)
        {
            /* Remember the first of the alternate APIs. */
            if ((first_alt = iff->first_alt) == NULL)
                first_alt = iff;

            break;
        }

        /*
         * They must be the same type except that we allow a class if we want
         * an exception.  This is because we allow classes to be used before
         * they are defined.
         */
        if (iff->type != iftype)
            if (iftype != exception_iface || iff->type != class_iface)
                yyerror("A class, exception, namespace or mapped type has already been defined with the same name");

        /* Ignore an external class declared in another module. */
        if (iftype == class_iface && iff->module != mod)
        {
            classDef *cd;

            for (cd = pt->classes; cd != NULL; cd = cd->next)
                if (cd->iff == iff)
                    break;

            if (cd != NULL && iff->module != NULL && isExternal(cd))
                continue;
        }

        /*
         * If this is a mapped type with the same name defined in a different
         * module, then check that this type isn't the same as any of the
         * mapped types defined in that module.
         */
        if (iftype == mappedtype_iface && iff->module != mod)
        {
            mappedTypeDef *mtd;

            /*
             * This is a bit of a cheat.  With consolidated modules it's
             * possible to have two implementations of a mapped type in
             * different branches of the module hierarchy.  We assume that, if
             * there really are multiple implementations in the same branch,
             * then it will be picked up in a non-consolidated build.
             */
            if (isConsolidated(pt->module))
                continue;

            for (mtd = pt->mappedtypes; mtd != NULL; mtd = mtd->next)
            {
                if (mtd->iff != iff)
                    continue;

                if (ad->atype != template_type ||
                    mtd->type.atype != template_type ||
                    sameBaseType(ad, &mtd->type))
                    yyerror("Mapped type has already been defined in another module");
            }

            /*
             * If we got here then we have a mapped type based on an existing
             * template, but with unique parameters.  We don't want to use
             * interface files from other modules, so skip this one.
             */

            continue;
        }

        /* Ignore a namespace defined in another module. */
        if (iftype == namespace_iface && iff->module != mod)
            continue;

        return iff;
    }

    iff = sipMalloc(sizeof (ifaceFileDef));

    iff->name = cacheName(pt, scopedNameToString(fqname));
    iff->api_range = api_range;

    if (first_alt != NULL)
    {
        iff->first_alt = first_alt;
        iff->next_alt = first_alt->next_alt;

        first_alt->next_alt = iff;
    }
    else
    {
        /* This is the first alternate so point to itself. */
        iff->first_alt = iff;
    }

    iff->type = iftype;
    iff->ifacenr = -1;
    iff->fqcname = fqname;
    iff->module = NULL;
    iff->hdrcode = NULL;
    iff->used = NULL;
    iff->file_extension = NULL;
    iff->next = pt->ifacefiles;

    pt->ifacefiles = iff;

    return iff;
}


/*
 * Find a class definition in a parse tree.
 */
static classDef *findClass(sipSpec *pt, ifaceFileType iftype,
        apiVersionRangeDef *api_range, scopedNameDef *fqname)
{
    return findClassWithInterface(pt, findIfaceFile(pt, currentModule, fqname, iftype, api_range, NULL));
}


/*
 * Find a class definition given an existing interface file.
 */
static classDef *findClassWithInterface(sipSpec *pt, ifaceFileDef *iff)
{
    classDef *cd;

    for (cd = pt -> classes; cd != NULL; cd = cd -> next)
        if (cd -> iff == iff)
            return cd;

    /* Create a new one. */
    cd = sipMalloc(sizeof (classDef));

    cd->iff = iff;
    cd->pyname = cacheName(pt, classBaseName(cd));
    cd->next = pt->classes;

    pt->classes = cd;

    return cd;
}


/*
 * Add an interface file to an interface file list if it isn't already there.
 */
void appendToIfaceFileList(ifaceFileList **ifflp, ifaceFileDef *iff)
{
    /* Make sure we don't try to add an interface file to its own list. */
    if (&iff->used != ifflp)
    {
        ifaceFileList *iffl;

        while ((iffl = *ifflp) != NULL)
        {
            /* Don't bother if it is already there. */
            if (iffl->iff == iff)
                return;

            ifflp = &iffl -> next;
        }

        iffl = sipMalloc(sizeof (ifaceFileList));

        iffl->iff = iff;
        iffl->next = NULL;

        *ifflp = iffl;
    }
}


/*
 * Find an undefined (or create a new) exception definition in a parse tree.
 */
static exceptionDef *findException(sipSpec *pt, scopedNameDef *fqname, int new)
{
    exceptionDef *xd, **tail;
    ifaceFileDef *iff;
    classDef *cd;

    iff = findIfaceFile(pt, currentModule, fqname, exception_iface, NULL, NULL);

    /* See if it is an existing one. */
    for (xd = pt->exceptions; xd != NULL; xd = xd->next)
        if (xd->iff == iff)
            return xd;

    /*
     * If it is an exception interface file then we have never seen this name
     * before.  We require that exceptions are defined before being used, but
     * don't make the same requirement of classes (for reasons of backwards
     * compatibility).  Therefore the name must be reinterpreted as a (as yet
     * undefined) class.
     */
    if (new)
    {
        if (iff->type == exception_iface)
            cd = NULL;
        else
            yyerror("There is already a class with the same name or the exception has been used before being defined");
    }
    else
    {
        if (iff->type == exception_iface)
            iff->type = class_iface;

        cd = findClassWithInterface(pt, iff);
    }

    /* Create a new one. */
    xd = sipMalloc(sizeof (exceptionDef));

    xd->exceptionnr = -1;
    xd->iff = iff;
    xd->pyname = NULL;
    xd->cd = cd;
    xd->bibase = NULL;
    xd->base = NULL;
    xd->raisecode = NULL;
    xd->next = NULL;

    /* Append it to the list. */
    for (tail = &pt->exceptions; *tail != NULL; tail = &(*tail)->next)
        ;

    *tail = xd;

    return xd;
}


/*
 * Find an undefined (or create a new) class definition in a parse tree.
 */
static classDef *newClass(sipSpec *pt, ifaceFileType iftype,
        apiVersionRangeDef *api_range, scopedNameDef *fqname,
        const char *virt_error_handler, typeHintDef *typehint_in,
        typeHintDef *typehint_out, const char *typehint_value)
{
    int flags;
    classDef *cd, *scope;
    codeBlockList *hdrcode;

    if (sectionFlags & SECT_IS_PRIVATE)
        yyerror("Classes, structs and namespaces must be in the public or protected sections");

    flags = 0;

    if ((scope = currentScope()) != NULL)
    {
        if (sectionFlags & SECT_IS_PROT && !makeProtPublic)
        {
            flags = CLASS_IS_PROTECTED;

            if (scope->iff->type == class_iface)
                setHasShadow(scope);
        }

        /* Header code from outer scopes is also included. */
        hdrcode = scope->iff->hdrcode;
    }
    else
        hdrcode = NULL;

    if (pt -> genc)
    {
        /* C structs are always global types. */
        while (fqname -> next != NULL)
            fqname = fqname -> next;

        scope = NULL;
    }

    cd = findClass(pt, iftype, api_range, fqname);

    /* Check it hasn't already been defined. */
    if (iftype != namespace_iface && cd->iff->module != NULL)
        yyerror("The struct/class has already been defined");

    /* Complete the initialisation. */
    cd->classflags |= flags;
    cd->ecd = scope;
    cd->iff->module = currentModule;
    cd->virt_error_handler = virt_error_handler;
    cd->typehint_in = typehint_in;
    cd->typehint_out = typehint_out;
    cd->typehint_value = typehint_value;

    if (currentIsTemplate)
        setIsTemplateClass(cd);

    appendCodeBlockList(&cd->iff->hdrcode, hdrcode);

    /* See if it is a namespace extender. */
    if (iftype == namespace_iface)
    {
        classDef *ns;

        for (ns = pt->classes; ns != NULL; ns = ns->next)
        {
            if (ns == cd)
                continue;

            if (ns->iff->type != namespace_iface)
                continue;

            if (compareScopedNames(ns->iff->fqcname, fqname) != 0)
                continue;

            cd->real = ns;
            break;
        }
    }

    return cd;
}


/*
 * Tidy up after finishing a class definition.
 */
static void finishClass(sipSpec *pt, moduleDef *mod, classDef *cd,
        optFlags *of)
{
    const char *pyname;
    optFlag *flg;

    /* Get the Python name and see if it is different to the C++ name. */
    pyname = getPythonName(mod, of, classBaseName(cd));

    cd->pyname = NULL;
    checkAttributes(pt, mod, cd->ecd, NULL, pyname, FALSE);
    cd->pyname = cacheName(pt, pyname);
    cd->no_typehint = getNoTypeHint(of);

    if ((flg = getOptFlag(of, "Metatype", dotted_name_flag)) != NULL)
        cd->metatype = cacheName(pt, flg->fvalue.sval);

    if ((flg = getOptFlag(of, "Supertype", dotted_name_flag)) != NULL)
        cd->supertype = cacheName(pt, flg->fvalue.sval);

    if (getOptFlag(of, "ExportDerived", bool_flag) != NULL)
        setExportDerived(cd);

    if (getOptFlag(of, "Mixin", bool_flag) != NULL)
        setMixin(cd);

    if ((flg = getOptFlag(of, "FileExtension", string_flag)) != NULL)
        cd->iff->file_extension = flg->fvalue.sval;

    if ((flg = getOptFlag(of, "PyQtFlags", integer_flag)) != NULL)
        cd->pyqt_flags = flg->fvalue.ival;

    if (getOptFlag(of, "PyQtNoQMetaObject", bool_flag) != NULL)
        setPyQtNoQMetaObject(cd);

    if ((flg = getOptFlag(of, "PyQtInterface", string_flag)) != NULL)
        cd->pyqt_interface = flg->fvalue.sval;

    if (isOpaque(cd))
    {
        if (getOptFlag(of, "External", bool_flag) != NULL)
            setIsExternal(cd);
    }
    else
    {
        int seq_might, seq_not, default_to_sequence;
        memberDef *md;

        if (getOptFlag(of, "NoDefaultCtors", bool_flag) != NULL)
            setNoDefaultCtors(cd);

        if (cd -> ctors == NULL)
        {
            if (!noDefaultCtors(cd))
            {
                /* Provide a default ctor. */

                cd->ctors = sipMalloc(sizeof (ctorDef));
 
                cd->ctors->ctorflags = SECT_IS_PUBLIC;
                cd->ctors->pysig.result.atype = void_type;
                cd->ctors->cppsig = &cd->ctors->pysig;

                cd->defctor = cd->ctors;

                setCanCreate(cd);
            }
        }
        else if (cd -> defctor == NULL)
        {
            ctorDef *ct, *last = NULL;

            for (ct = cd -> ctors; ct != NULL; ct = ct -> next)
            {
                if (!isPublicCtor(ct))
                    continue;

                if (ct -> pysig.nrArgs == 0 || ct -> pysig.args[0].defval != NULL)
                {
                    cd -> defctor = ct;
                    break;
                }

                if (last == NULL)
                    last = ct;
            }

            /* The last resort is the first public ctor. */
            if (cd->defctor == NULL)
                cd->defctor = last;
        }

        if (getDeprecated(of))
            setIsDeprecatedClass(cd);

        if (cd->convtocode != NULL && getAllowNone(of))
            setClassHandlesNone(cd);

        if (getOptFlag(of,"Abstract",bool_flag) != NULL)
        {
            setIsAbstractClass(cd);
            setIsIncomplete(cd);
            resetCanCreate(cd);
        }

        /* We assume a public dtor if nothing specific was provided. */
        if (!isDtor(cd))
            setIsPublicDtor(cd);

        if (getOptFlag(of, "DelayDtor", bool_flag) != NULL)
        {
            setIsDelayedDtor(cd);
            setHasDelayedDtors(mod);
        }

        /*
         * There are subtle differences between the add and concat methods and
         * the multiply and repeat methods.  The number versions can have their
         * operands swapped and may return NotImplemented.  If the user has
         * used the /Numeric/ annotation or there are other numeric operators
         * then we use add/multiply.  Otherwise, if the user has used the
         * /Sequence/ annotation or there are indexing operators then we use
         * concat/repeat.
         */
        seq_might = seq_not = FALSE;

        for (md = cd->members; md != NULL; md = md->next)
            switch (md->slot)
            {
            case getitem_slot:
            case setitem_slot:
            case delitem_slot:
                /* This might be a sequence. */
                seq_might = TRUE;
                break;

            case sub_slot:
            case isub_slot:
            case div_slot:
            case idiv_slot:
            case mod_slot:
            case imod_slot:
            case floordiv_slot:
            case ifloordiv_slot:
            case truediv_slot:
            case itruediv_slot:
            case pos_slot:
            case neg_slot:
                /* This is definately not a sequence. */
                seq_not = TRUE;
                break;

            /* Suppress a compiler warning. */
            default:
                ;
            }

        default_to_sequence = (!seq_not && seq_might);

        for (md = cd->members; md != NULL; md = md->next)
        {
            /* Ignore if it is explicitly numeric. */
            if (isNumeric(md))
                continue;

            if (isSequence(md) || default_to_sequence)
                switch (md->slot)
                {
                case add_slot:
                    md->slot = concat_slot;
                    break;

                case iadd_slot:
                    md->slot = iconcat_slot;
                    break;

                case mul_slot:
                    md->slot = repeat_slot;
                    break;

                case imul_slot:
                    md->slot = irepeat_slot;
                    break;

                /* Suppress a compiler warning. */
                default:
                    ;
                }
        }
    }

    if (inMainModule())
    {
        setIsUsedName(cd->iff->name);
        setIsUsedName(cd->pyname);
    }
}


/*
 * Return the encoded name of a template (ie. including its argument types) as
 * a scoped name.
 */
scopedNameDef *encodedTemplateName(templateDef *td)
{
    int a;
    scopedNameDef *snd;

    snd = copyScopedName(td->fqname);

    for (a = 0; a < td->types.nrArgs; ++a)
    {
        char buf[50];
        int flgs;
        scopedNameDef *arg_snd;
        argDef *ad = &td->types.args[a];

        flgs = 0;

        if (isConstArg(ad))
            flgs += 1;

        if (isReference(ad))
            flgs += 2;

        /* We use numbers so they don't conflict with names. */
        sprintf(buf, "%02d%d%d", ad->atype, flgs, ad->nrderefs);

        switch (ad->atype)
        {
        case defined_type:
            arg_snd = copyScopedName(ad->u.snd);
            break;

        case template_type:
            arg_snd = encodedTemplateName(ad->u.td);
            break;

        case struct_type:
            arg_snd = copyScopedName(ad->u.sname);
            break;

        default:
            arg_snd = NULL;
        }

        /*
         * Replace the first element of the argument name with a copy with the
         * encoding prepended.
         */
        if (arg_snd != NULL)
            arg_snd->name = concat(buf, arg_snd->name, NULL);
        else
            arg_snd = text2scopePart(sipStrdup(buf));

        appendScopedName(&snd, arg_snd);
    }

    return snd;
}


/*
 * Create a new mapped type.
 */
static mappedTypeDef *newMappedType(sipSpec *pt, argDef *ad, optFlags *of)
{
    mappedTypeDef *mtd;
    scopedNameDef *snd;
    ifaceFileDef *iff;
    const char *cname;

    /* Check that the type is one we want to map. */
    switch (ad->atype)
    {
    case defined_type:
        snd = ad->u.snd;
        cname = scopedNameTail(snd);
        break;

    case template_type:
        snd = encodedTemplateName(ad->u.td);
        cname = NULL;
        break;

    case struct_type:
        snd = ad->u.sname;
        cname = scopedNameTail(snd);
        break;

    default:
        yyerror("Invalid type for %MappedType");
    }

    iff = findIfaceFile(pt, currentModule, snd, mappedtype_iface,
            getAPIRange(of), ad);

    /* Check it hasn't already been defined. */
    for (mtd = pt->mappedtypes; mtd != NULL; mtd = mtd->next)
        if (mtd->iff == iff)
        {
            /*
             * We allow types based on the same template but with different
             * arguments.
             */
            if (ad->atype != template_type || sameBaseType(ad, &mtd->type))
                yyerror("Mapped type has already been defined in this module");
        }

    /* The module may not have been set yet. */
    iff->module = currentModule;

    /* Create a new mapped type. */
    mtd = allocMappedType(pt, ad);

    if (cname != NULL)
        mtd->pyname = cacheName(pt, getPythonName(currentModule, of, cname));

    mappedTypeAnnos(mtd, of);

    mtd->iff = iff;
    mtd->next = pt->mappedtypes;

    pt->mappedtypes = mtd;

    if (inMainModule())
    {
        setIsUsedName(mtd->cname);

        if (mtd->pyname)
            setIsUsedName(mtd->pyname);
    }

    return mtd;
}


/*
 * Allocate, initialise and return a mapped type structure.
 */
mappedTypeDef *allocMappedType(sipSpec *pt, argDef *type)
{
    mappedTypeDef *mtd;

    mtd = sipMalloc(sizeof (mappedTypeDef));

    mtd->type = *type;
    mtd->type.argflags = 0;
    mtd->type.nrderefs = 0;

    mtd->cname = cacheName(pt, type2string(&mtd->type));

    return mtd;
}


/*
 * Create a new enum.
 */
static enumDef *newEnum(sipSpec *pt, moduleDef *mod, mappedTypeDef *mt_scope,
        char *name, optFlags *of, int flags)
{
    enumDef *ed, *first_alt, *next_alt;
    classDef *c_scope;
    ifaceFileDef *scope;

    if (mt_scope != NULL)
    {
        scope = mt_scope->iff;
        c_scope = NULL;
    }
    else
    {
        if ((c_scope = currentScope()) != NULL)
            scope = c_scope->iff;
        else
            scope = NULL;
    }

    ed = sipMalloc(sizeof (enumDef));

    /* Assume the enum isn't versioned. */
    first_alt = ed;
    next_alt = NULL;

    if (name != NULL)
    {
        ed->pyname = cacheName(pt, getPythonName(mod, of, name));
        checkAttributes(pt, mod, c_scope, mt_scope, ed->pyname->text, FALSE);

        ed->fqcname = text2scopedName(scope, name);
        ed->cname = cacheName(pt, scopedNameToString(ed->fqcname));

        if (inMainModule())
        {
            setIsUsedName(ed->pyname);
            setIsUsedName(ed->cname);
        }

        /* If the scope is versioned then look for any alternate. */
        if (scope != NULL && scope->api_range != NULL)
        {
            enumDef *alt;

            for (alt = pt->enums; alt != NULL; alt = alt->next)
            {
                if (alt->module != mod || alt->fqcname == NULL)
                    continue;

                if (compareScopedNames(alt->fqcname, ed->fqcname) == 0)
                {
                    first_alt = alt->first_alt;
                    next_alt = first_alt->next_alt;
                    first_alt->next_alt = ed;

                    break;
                }
            }
        }
    }
    else
    {
        ed->pyname = NULL;
        ed->fqcname = NULL;
        ed->cname = NULL;
    }

    if (flags & SECT_IS_PROT)
    {
        if (makeProtPublic)
        {
            flags &= ~SECT_IS_PROT;
            flags |= SECT_IS_PUBLIC;
        }
        else if (c_scope != NULL)
        {
            setHasShadow(c_scope);
        }
    }

    ed->enumflags = flags;
    ed->no_typehint = getNoTypeHint(of);
    ed->enumnr = -1;
    ed->ecd = c_scope;
    ed->emtd = mt_scope;
    ed->first_alt = first_alt;
    ed->next_alt = next_alt;
    ed->module = mod;
    ed->members = NULL;
    ed->slots = NULL;
    ed->overs = NULL;
    ed->next = pt -> enums;

    pt->enums = ed;

    if (getOptFlag(of, "NoScope", bool_flag) != NULL)
        setIsNoScope(ed);

    return ed;
}


/*
 * Get the type values and (optionally) the type names for substitution in
 * handwritten code.
 */
void appendTypeStrings(scopedNameDef *ename, signatureDef *patt, signatureDef *src, signatureDef *known, scopedNameDef **names, scopedNameDef **values)
{
    int a;

    for (a = 0; a < patt->nrArgs; ++a)
    {
        argDef *pad = &patt->args[a];

        if (pad->atype == defined_type)
        {
            char *nam = NULL, *val;
            argDef *sad;

            /*
             * If the type names are already known then check that this is one
             * of them.
             */
            if (known == NULL)
                nam = scopedNameTail(pad->u.snd);
            else if (pad->u.snd->next == NULL)
            {
                int k;

                for (k = 0; k < known->nrArgs; ++k)
                {
                    /* Skip base types. */
                    if (known->args[k].atype != defined_type)
                        continue;

                    if (strcmp(pad->u.snd->name, known->args[k].u.snd->name) == 0)
                    {
                        nam = pad->u.snd->name;
                        break;
                    }
                }
            }

            if (nam == NULL)
                continue;

            /* Add the name. */
            appendScopedName(names, text2scopePart(nam));

            /*
             * Add the corresponding value.  For defined types we don't want 
             * any indirection or references.
             */
            sad = &src->args[a];

            if (sad->atype == defined_type)
                val = scopedNameToString(sad->u.snd);
            else
                val = type2string(sad);

            /* We do want const. */
            if (isConstArg(sad))
            {
                char *const_val = sipStrdup("const ");

                append(&const_val, val);
                free(val);

                val = const_val;
            }

            appendScopedName(values, text2scopePart(val));
        }
        else if (pad->atype == template_type)
        {
            argDef *sad = &src->args[a];

            /* These checks shouldn't be necessary, but... */
            if (sad->atype == template_type && pad->u.td->types.nrArgs == sad->u.td->types.nrArgs)
                appendTypeStrings(ename, &pad->u.td->types, &sad->u.td->types, known, names, values);
        }
    }
}


/*
 * Convert a type to a string on the heap.  The string will use the minimum
 * whitespace while still remaining valid C++.
 */
static char *type2string(argDef *ad)
{
    int i, on_heap = FALSE;
    int nr_derefs = ad->nrderefs;
    int is_reference = isReference(ad);
    char *s;

    /* Use the original type if possible. */
    if (ad->original_type != NULL && !noTypeName(ad->original_type))
    {
        s = scopedNameToString(ad->original_type->fqname);
        on_heap = TRUE;

        nr_derefs -= ad->original_type->type.nrderefs;

        if (isReference(&ad->original_type->type))
            is_reference = FALSE;
    }
    else
        switch (ad->atype)
        {
        case template_type:
            {
                templateDef *td = ad->u.td;

                s = scopedNameToString(td->fqname);
                append(&s, "<");

                for (i = 0; i < td->types.nrArgs; ++i)
                {
                    char *sub_type = type2string(&td->types.args[i]);

                    if (i > 0)
                        append(&s, ",");

                    append(&s, sub_type);
                    free(sub_type);
                }

                if (s[strlen(s) - 1] == '>')
                    append(&s, " >");
                else
                    append(&s, ">");

                on_heap = TRUE;
                break;
            }

        case struct_type:
            s = scopedNameToString(ad->u.sname);
            on_heap = TRUE;
            break;

        case defined_type:
            s = scopedNameToString(ad->u.snd);
            on_heap = TRUE;
            break;

        case ubyte_type:
        case ustring_type:
            s = "unsigned char";
            break;

        case byte_type:
        case ascii_string_type:
        case latin1_string_type:
        case utf8_string_type:
        case string_type:
            s = "char";
            break;

        case sbyte_type:
        case sstring_type:
            s = "signed char";
            break;

        case wstring_type:
            s = "wchar_t";
            break;

        case ushort_type:
            s = "unsigned short";
            break;

        case short_type:
            s = "short";
            break;

        case uint_type:
            s = "uint";
            break;

        case int_type:
        case cint_type:
            s = "int";
            break;

        case ulong_type:
            s = "unsigned long";
            break;

        case long_type:
            s = "long";
            break;

        case ulonglong_type:
            s = "unsigned long long";
            break;

        case longlong_type:
            s = "long long";
            break;

        case float_type:
        case cfloat_type:
            s = "float";
            break;

        case double_type:
        case cdouble_type:
            s = "double";
            break;

        case bool_type:
        case cbool_type:
            s = "bool";
            break;

        case void_type:
            s = "void";
            break;

        case capsule_type:
            s = "void *";
            break;

        default:
            fatal("Unsupported type argument to type2string(): %d\n", ad->atype);
        }

    /* Make sure the string is on the heap. */
    if (!on_heap)
        s = sipStrdup(s);

    while (nr_derefs-- > 0)
        append(&s, "*");

    if (is_reference)
        append(&s, "&");

    return s;
}


/*
 * Convert a scoped name to a string on the heap.
 */
static char *scopedNameToString(scopedNameDef *name)
{
    static const char scope_string[] = "::";
    size_t len;
    scopedNameDef *snd;
    char *s, *dp;

    /* Work out the length of buffer needed. */
    len = 0;

    for (snd = name; snd != NULL; snd = snd->next)
    {
        len += strlen(snd->name);

        if (snd->next != NULL)
        {
            /* Ignore the encoded part of template names. */
            if (isdigit(snd->next->name[0]))
                break;

            len += strlen(scope_string);
        }
    }

    /* Allocate and populate the buffer. */
    dp = s = sipMalloc(len + 1);

    for (snd = name; snd != NULL; snd = snd->next)
    {
        strcpy(dp, snd->name);
        dp += strlen(snd->name);

        if (snd->next != NULL)
        {
            /* Ignore the encoded part of template names. */
            if (isdigit(snd->next->name[0]))
                break;

            strcpy(dp, scope_string);
            dp += strlen(scope_string);
        }
    }

    return s;
}


/*
 * Instantiate a class template.
 */
static void instantiateClassTemplate(sipSpec *pt, moduleDef *mod,
        classDef *scope, scopedNameDef *fqname, classTmplDef *tcd,
        templateDef *td, const char *pyname)
{
    scopedNameDef *type_names, *type_values;
    classDef *cd;
    ctorDef *oct, **cttail;
    argDef *ad;
    ifaceFileList *iffl, **used;
    classList *cl;

    type_names = type_values = NULL;
    appendTypeStrings(classFQCName(tcd->cd), &tcd->sig, &td->types, NULL, &type_names, &type_values);

    /*
     * Add a mapping from the template name to the instantiated name.  If we
     * have got this far we know there is room for it.
     */
    ad = &tcd->sig.args[tcd->sig.nrArgs++];
    memset(ad, 0, sizeof (argDef));
    ad->atype = defined_type;
    ad->u.snd = classFQCName(tcd->cd);

    appendScopedName(&type_names, text2scopePart(scopedNameTail(classFQCName(tcd->cd))));
    appendScopedName(&type_values, text2scopePart(scopedNameToString(fqname)));

    /* Create the new class. */
    cd = sipMalloc(sizeof (classDef));

    /* Start with a shallow copy. */
    *cd = *tcd->cd;

    resetIsTemplateClass(cd);
    cd->pyname = cacheName(pt, pyname);
    cd->td = td;

    /* Handle the interface file. */
    cd->iff = findIfaceFile(pt, mod, fqname, class_iface,
            (scope != NULL ? scope->iff->api_range : NULL), NULL);
    cd->iff->module = mod;

    appendCodeBlockList(&cd->iff->hdrcode, tcd->cd->iff->hdrcode);

    /* Make a copy of the used list and add the enclosing scope. */
    used = &cd->iff->used;

    for (iffl = tcd->cd->iff->used; iffl != NULL; iffl = iffl->next)
        appendToIfaceFileList(used, iffl->iff);

    /* Include any scope header code. */
    if (scope != NULL)
        appendCodeBlockList(&cd->iff->hdrcode, scope->iff->hdrcode);

    if (inMainModule())
    {
        setIsUsedName(cd->iff->name);
        setIsUsedName(cd->pyname);
    }

    cd->ecd = currentScope();

    /* Handle any type hints. */
    if (cd->typehint_in != NULL)
        cd->typehint_in = newTypeHint(
                templateString(cd->typehint_in->raw_hint, type_names,
                        type_values));

    if (cd->typehint_out != NULL)
        cd->typehint_out = newTypeHint(
                templateString(cd->typehint_out->raw_hint, type_names,
                        type_values));

    /* Handle the super-classes. */
    for (cl = cd->supers; cl != NULL; cl = cl->next)
    {
        const char *name;
        int a;

        /* Ignore defined or scoped classes. */
        if (cl->cd->iff->module != NULL || cl->cd->iff->fqcname->next != NULL)
            continue;

        name = cl->cd->iff->fqcname->name;

        for (a = 0; a < tcd->sig.nrArgs - 1; ++a)
            if (strcmp(name, scopedNameTail(tcd->sig.args[a].u.snd)) == 0)
            {
                argDef *tad = &td->types.args[a];
                classDef *icd;

                if (tad->atype == defined_type)
                    icd = findClass(pt, class_iface, NULL, tad->u.snd);
                else if (tad->atype == class_type)
                    icd = tad->u.cd;
                else
                    fatal("Template argument %s must expand to a class\n", name);

                /*
                 * Don't complain about the template argument being undefined.
                 */
                setTemplateArg(cl->cd);

                cl->cd = icd;
            }
    }

    /* Handle the enums. */
    instantiateTemplateEnums(pt, tcd, td, cd, used, type_names, type_values);

    /* Handle the variables. */
    instantiateTemplateVars(pt, tcd, td, cd, used, type_names, type_values);

    /* Handle the typedefs. */
    instantiateTemplateTypedefs(pt, tcd, td, cd, type_names, type_values);

    /* Handle the ctors. */
    cd->ctors = NULL;
    cttail = &cd->ctors;

    for (oct = tcd->cd->ctors; oct != NULL; oct = oct->next)
    {
        ctorDef *nct = sipMalloc(sizeof (ctorDef));

        /* Start with a shallow copy. */
        *nct = *oct;

        templateSignature(&nct->pysig, FALSE, tcd, td, cd, type_names,
                type_values);

        if (oct->cppsig == NULL)
            nct->cppsig = NULL;
        else if (oct->cppsig == &oct->pysig)
            nct->cppsig = &nct->pysig;
        else
        {
            nct->cppsig = sipMalloc(sizeof (signatureDef));

            *nct->cppsig = *oct->cppsig;

            templateSignature(nct->cppsig, FALSE, tcd, td, cd, type_names,
                    type_values);
        }

        nct->methodcode = templateCode(pt, used, nct->methodcode, type_names, type_values);

        nct->next = NULL;
        *cttail = nct;
        cttail = &nct->next;

        /* Handle the default ctor. */
        if (tcd->cd->defctor == oct)
            cd->defctor = nct;
    }

    cd->dealloccode = templateCode(pt, used, cd->dealloccode, type_names, type_values);
    cd->dtorcode = templateCode(pt, used, cd->dtorcode, type_names, type_values);

    /* Handle the methods. */
    cd->members = instantiateTemplateMethods(tcd->cd->members, mod);
    cd->overs = instantiateTemplateOverloads(pt, tcd->cd->overs,
            tcd->cd->members, cd->members, tcd, td, cd, used, type_names,
            type_values);

    cd->cppcode = templateCode(pt, used, cd->cppcode, type_names, type_values);
    cd->iff->hdrcode = templateCode(pt, used, cd->iff->hdrcode, type_names, type_values);
    cd->convtosubcode = templateCode(pt, used, cd->convtosubcode, type_names, type_values);
    cd->convtocode = templateCode(pt, used, cd->convtocode, type_names, type_values);
    cd->travcode = templateCode(pt, used, cd->travcode, type_names, type_values);
    cd->clearcode = templateCode(pt, used, cd->clearcode, type_names, type_values);
    cd->getbufcode = templateCode(pt, used, cd->getbufcode, type_names, type_values);
    cd->releasebufcode = templateCode(pt, used, cd->releasebufcode, type_names, type_values);
    cd->readbufcode = templateCode(pt, used, cd->readbufcode, type_names, type_values);
    cd->writebufcode = templateCode(pt, used, cd->writebufcode, type_names, type_values);
    cd->segcountcode = templateCode(pt, used, cd->segcountcode, type_names, type_values);
    cd->charbufcode = templateCode(pt, used, cd->charbufcode, type_names, type_values);
    cd->instancecode = templateCode(pt, used, cd->instancecode, type_names, type_values);
    cd->picklecode = templateCode(pt, used, cd->picklecode, type_names, type_values);
    cd->finalcode = templateCode(pt, used, cd->finalcode, type_names, type_values);
    cd->typehintcode = templateCode(pt, used, cd->typehintcode, type_names, type_values);
    cd->next = pt->classes;

    pt->classes = cd;

    tcd->sig.nrArgs--;

    freeScopedName(type_names);
    freeScopedName(type_values);
}


/*
 * Instantiate the methods of a template class.
 */
static memberDef *instantiateTemplateMethods(memberDef *tmd, moduleDef *mod)
{
    memberDef *md, *methods, **mdtail;

    methods = NULL;
    mdtail = &methods;

    for (md = tmd; md != NULL; md = md->next)
    {
        memberDef *nmd = sipMalloc(sizeof (memberDef));

        /* Start with a shallow copy. */
        *nmd = *md;

        nmd->module = mod;

        if (inMainModule())
            setIsUsedName(nmd->pyname);

        nmd->next = NULL;
        *mdtail = nmd;
        mdtail = &nmd->next;
    }

    return methods;
}


/*
 * Instantiate the overloads of a template class.
 */
static overDef *instantiateTemplateOverloads(sipSpec *pt, overDef *tod,
        memberDef *tmethods, memberDef *methods, classTmplDef *tcd,
        templateDef *td, classDef *cd, ifaceFileList **used,
        scopedNameDef *type_names, scopedNameDef *type_values)
{
    overDef *od, *overloads, **odtail;

    overloads = NULL;
    odtail = &overloads;

    for (od = tod; od != NULL; od = od->next)
    {
        overDef *nod = sipMalloc(sizeof (overDef));
        memberDef *nmd, *omd;

        /* Start with a shallow copy. */
        *nod = *od;

        for (nmd = methods, omd = tmethods; omd != NULL; omd = omd->next, nmd = nmd->next)
            if (omd == od->common)
            {
                nod->common = nmd;
                break;
            }

        templateSignature(&nod->pysig, TRUE, tcd, td, cd, type_names,
                type_values);

        if (od->cppsig == &od->pysig)
            nod->cppsig = &nod->pysig;
        else
        {
            nod->cppsig = sipMalloc(sizeof (signatureDef));

            *nod->cppsig = *od->cppsig;

            templateSignature(nod->cppsig, TRUE, tcd, td, cd, type_names,
                    type_values);
        }

        nod->methodcode = templateCode(pt, used, nod->methodcode, type_names, type_values);
        nod->virtcallcode = templateCode(pt, used, nod->virtcallcode, type_names, type_values);

        /* Handle any virtual handler. */
        if (od->virthandler != NULL)
        {
            moduleDef *mod = cd->iff->module;

            nod->virthandler = sipMalloc(sizeof (virtHandlerDef));

            /* Start with a shallow copy. */
            *nod->virthandler = *od->virthandler;

            nod->virthandler->pysig = &nod->pysig;
            nod->virthandler->cppsig = nod->cppsig;

            nod->virthandler->module = mod;
            nod->virthandler->virtcode = templateCode(pt, used, nod->virthandler->virtcode, type_names, type_values);
            nod->virthandler->next = mod->virthandlers;

            mod->virthandlers = nod->virthandler;
        }

        nod->next = NULL;
        *odtail = nod;
        odtail = &nod->next;
    }

    return overloads;
}


/*
 * Instantiate the enums of a template class.
 */
static void instantiateTemplateEnums(sipSpec *pt, classTmplDef *tcd,
        templateDef *td, classDef *cd, ifaceFileList **used,
        scopedNameDef *type_names, scopedNameDef *type_values)
{
    enumDef *ted;
    moduleDef *mod = cd->iff->module;

    for (ted = pt->enums; ted != NULL; ted = ted->next)
        if (ted->ecd == tcd->cd)
        {
            enumDef *ed;
            enumMemberDef *temd;

            ed = sipMalloc(sizeof (enumDef));

            /* Start with a shallow copy. */
            *ed = *ted;

            if (ed->fqcname != NULL)
            {
                ed->fqcname = text2scopedName(cd->iff,
                        scopedNameTail(ed->fqcname));
                ed->cname = cacheName(pt, scopedNameToString(ed->fqcname));
            }

            if (inMainModule())
            {
                if (ed->pyname != NULL)
                    setIsUsedName(ed->pyname);

                if (ed->cname != NULL)
                    setIsUsedName(ed->cname);
            }

            ed->ecd = cd;
            ed->first_alt = ed;
            ed->module = mod;
            ed->members = NULL;

            for (temd = ted->members; temd != NULL; temd = temd->next)
            {
                enumMemberDef *emd;

                emd = sipMalloc(sizeof (enumMemberDef));

                /* Start with a shallow copy. */
                *emd = *temd;
                emd->ed = ed;

                emd->next = ed->members;
                ed->members = emd;
            }

            ed->slots = instantiateTemplateMethods(ted->slots, mod);
            ed->overs = instantiateTemplateOverloads(pt, ted->overs,
                    ted->slots, ed->slots, tcd, td, cd, used, type_names,
                    type_values);

            ed->next = pt->enums;
            pt->enums = ed;
        }
}


/*
 * Instantiate the variables of a template class.
 */
static void instantiateTemplateVars(sipSpec *pt, classTmplDef *tcd,
        templateDef *td, classDef *cd, ifaceFileList **used,
        scopedNameDef *type_names, scopedNameDef *type_values)
{
    varDef *tvd;

    for (tvd = pt->vars; tvd != NULL; tvd = tvd->next)
        if (tvd->ecd == tcd->cd)
        {
            varDef *vd;

            vd = sipMalloc(sizeof (varDef));

            /* Start with a shallow copy. */
            *vd = *tvd;

            if (inMainModule())
                setIsUsedName(vd->pyname);

            vd->fqcname = text2scopedName(cd->iff,
                    scopedNameTail(vd->fqcname));
            vd->ecd = cd;
            vd->module = cd->iff->module;

            templateType(&vd->type, tcd, td, cd, type_names, type_values);

            vd->accessfunc = templateCode(pt, used, vd->accessfunc, type_names, type_values);
            vd->getcode = templateCode(pt, used, vd->getcode, type_names, type_values);
            vd->setcode = templateCode(pt, used, vd->setcode, type_names, type_values);

            addVariable(pt, vd);
        }
}


/*
 * Instantiate the typedefs of a template class.
 */
static void instantiateTemplateTypedefs(sipSpec *pt, classTmplDef *tcd,
        templateDef *td, classDef *cd, scopedNameDef *type_names,
        scopedNameDef *type_values)
{
    typedefDef *tdd;

    for (tdd = pt->typedefs; tdd != NULL; tdd = tdd->next)
    {
        typedefDef *new_tdd;

        if (tdd->ecd != tcd->cd)
            continue;

        new_tdd = sipMalloc(sizeof (typedefDef));

        /* Start with a shallow copy. */
        *new_tdd = *tdd;

        new_tdd->fqname = text2scopedName(cd->iff,
                scopedNameTail(new_tdd->fqname));
        new_tdd->ecd = cd;
        new_tdd->module = cd->iff->module;

        templateType(&new_tdd->type, tcd, td, cd, type_names, type_values);

        addTypedef(pt, new_tdd);
    }
}


/*
 * Replace any template arguments in a signature.
 */
static void templateSignature(signatureDef *sd, int result, classTmplDef *tcd,
        templateDef *td, classDef *ncd, scopedNameDef *type_names,
        scopedNameDef *type_values)
{
    int a;

    if (result)
        templateType(&sd->result, tcd, td, ncd, type_names, type_values);

    for (a = 0; a < sd->nrArgs; ++a)
        templateType(&sd->args[a], tcd, td, ncd, type_names, type_values);
}


/*
 * Replace any template arguments in a type.
 */
static void templateType(argDef *ad, classTmplDef *tcd, templateDef *td,
        classDef *ncd, scopedNameDef *type_names, scopedNameDef *type_values)
{
    int a;
    char *name;

    /* Descend into any sub-templates. */
    if (ad->atype == template_type)
    {
        templateDef *new_td = sipMalloc(sizeof (templateDef));

        /* Make a deep copy of the template definition. */
        *new_td = *ad->u.td;
        ad->u.td = new_td;

        templateSignature(&ad->u.td->types, FALSE, tcd, td, ncd, type_names,
                type_values);

        return;
    }

    /* Handle any type hints. */
    if (ad->typehint_in != NULL)
        ad->typehint_in = newTypeHint(
                templateString(ad->typehint_in->raw_hint, type_names,
                        type_values));

    if (ad->typehint_out != NULL)
        ad->typehint_out = newTypeHint(
                templateString(ad->typehint_out->raw_hint, type_names,
                        type_values));

    /* Ignore if it isn't an unscoped name. */
    if (ad->atype != defined_type || ad->u.snd->next != NULL)
        return;

    name = ad->u.snd->name;

    for (a = 0; a < tcd->sig.nrArgs - 1; ++a)
        if (strcmp(name, scopedNameTail(tcd->sig.args[a].u.snd)) == 0)
        {
            argDef *tad = &td->types.args[a];

            ad->atype = tad->atype;

            /* We take the constrained flag from the real type. */
            resetIsConstrained(ad);

            if (isConstrained(tad))
                setIsConstrained(ad);

            ad->u = tad->u;

            return;
        }

    /* Handle the class name itself. */
    if (strcmp(name, scopedNameTail(classFQCName(tcd->cd))) == 0)
    {
        ad->atype = class_type;
        ad->u.cd = ncd;
        ad->original_type = NULL;
    }
}


/*
 * Replace any template arguments in a literal code block.
 */
codeBlockList *templateCode(sipSpec *pt, ifaceFileList **used,
        codeBlockList *ocbl, scopedNameDef *names, scopedNameDef *values)
{
    codeBlockList *ncbl = NULL;

    while (ocbl != NULL)
    {
        char *at = ocbl->block->frag;
        int start_of_line = TRUE;

        do
        {
            char *from = at, *first = NULL;
            codeBlock *cb;
            scopedNameDef *nam, *val, *nam_first, *val_first;

            /* Suppress a compiler warning. */
            val_first = NULL;

            /*
             * Don't do any substitution in lines that appear to be
             * preprocessor directives.  This prevents #include'd file names
             * being broken.
             */
            if (start_of_line)
            {
                /* Strip leading whitespace. */
                while (isspace(*from))
                    ++from;

                if (*from == '#')
                {
                    /* Skip to the end of the line. */
                    do
                        ++from;
                    while (*from != '\n' && *from != '\0');
                }
                else
                {
                    start_of_line = FALSE;
                }
            }

            /*
             * Go through the rest of this fragment looking for each of the
             * types and the name of the class itself.
             */
            nam = names;
            val = values;

            while (nam != NULL && val != NULL)
            {
                char *cp;

                if ((cp = strstr(from, nam->name)) != NULL)
                    if (first == NULL || first > cp)
                    {
                        nam_first = nam;
                        val_first = val;
                        first = cp;
                    }

                nam = nam->next;
                val = val->next;
            }

            /* Create the new fragment. */
            cb = sipMalloc(sizeof (codeBlock));

            if (at == ocbl->block->frag)
            {
                cb->filename = ocbl->block->filename;
                cb->linenr = ocbl->block->linenr;
            }
            else
                cb->filename = NULL;

            appendCodeBlock(&ncbl, cb);

            /* See if anything was found. */
            if (first == NULL)
            {
                /* We can just point to this. */
                cb->frag = at;

                /* All done with this one. */
                at = NULL;
            }
            else
            {
                static char *gen_names[] = {
                    "sipType_",
                    "sipClass_",
                    "sipEnum_",
                    "sipException_",
                    NULL
                };

                char *dp, *sp, **gn;
                int genname = FALSE;

                /*
                 * If the context in which the text is used is in the name of a
                 * SIP generated object then translate any "::" scoping to "_"
                 * and remove any const.
                 */
                for (gn = gen_names; *gn != NULL; ++gn)
                    if (search_back(first, at, *gn))
                    {
                        addUsedFromCode(pt, used, val_first->name);
                        genname = TRUE;
                        break;
                    }

                /* Fragment the fragment. */
                cb->frag = sipMalloc(first - at + strlen(val_first->name) + 1);

                strncpy(cb->frag, at, first - at);

                dp = &cb->frag[first - at];
                sp = val_first->name;

                if (genname)
                {
                    char gch;

                    if (strlen(sp) > 6 && strncmp(sp, "const ", 6) == 0)
                        sp += 6;

                    while ((gch = *sp++) != '\0')
                        if (gch == ':' && *sp == ':')
                        {
                            *dp++ = '_';
                            ++sp;
                        }
                        else
                            *dp++ = gch;

                    *dp = '\0';
                }
                else
                    strcpy(dp, sp);

                /* Move past the replaced text. */
                at = first + strlen(nam_first->name);

                if (*at == '\n')
                    start_of_line = TRUE;
            }
        }
        while (at != NULL && *at != '\0');

        ocbl = ocbl->next;
    }

    return ncbl;
}


/*
 * Return TRUE if the text at the end of a string matches the target string.
 */
static int search_back(const char *end, const char *start, const char *target)
{
    size_t tlen = strlen(target);

    if (start + tlen >= end)
        return FALSE;

    return (strncmp(end - tlen, target, tlen) == 0);
}


/*
 * Add any needed interface files based on handwritten code.
 */
static void addUsedFromCode(sipSpec *pt, ifaceFileList **used, const char *sname)
{
    ifaceFileDef *iff;
    enumDef *ed;

    for (iff = pt->ifacefiles; iff != NULL; iff = iff->next)
    {
        if (iff->type != class_iface && iff->type != exception_iface)
            continue;

        if (sameName(iff->fqcname, sname))
        {
            appendToIfaceFileList(used, iff);
            return;
        }
    }

    for (ed = pt->enums; ed != NULL; ed = ed->next)
    {
        if (ed->ecd == NULL)
            continue;

        if (sameName(ed->fqcname, sname))
        {
            appendToIfaceFileList(used, ed->ecd->iff);
            return;
        }
    }
}


/*
 * Compare a scoped name with its string equivalent.
 */
static int sameName(scopedNameDef *snd, const char *sname)
{
    while (snd != NULL && *sname != '\0')
    {
        const char *sp = snd->name;

        while (*sp != '\0' && *sname != ':' && *sname != '\0')
            if (*sp++ != *sname++)
                return FALSE;

        if (*sp != '\0' || (*sname != ':' && *sname != '\0'))
            return FALSE;

        snd = snd->next;

        if (*sname == ':')
            sname += 2;
    }

    return (snd == NULL && *sname == '\0');
}


/*
 * Compare a (possibly) relative scoped name with a fully qualified scoped name
 * while taking the current scope into account.
 */
static int foundInScope(scopedNameDef *fq_name, scopedNameDef *rel_name)
{
    classDef *scope;

    for (scope = currentScope(); scope != NULL; scope = scope->ecd)
    {
        scopedNameDef *snd;
        int found;

        snd = copyScopedName(classFQCName(scope));
        appendScopedName(&snd, copyScopedName(rel_name));

        found = (compareScopedNames(fq_name, snd) == 0);

        freeScopedName(snd);

        if (found)
            return TRUE;
    }

    return compareScopedNames(fq_name, rel_name) == 0;
}


/*
 * Create a new typedef.
 */
static void newTypedef(sipSpec *pt, moduleDef *mod, char *name, argDef *type,
        optFlags *optflgs)
{
    typedefDef *td;
    scopedNameDef *fqname;
    classDef *scope;

    scope = currentScope();
    fqname = text2scopedName((scope != NULL ? scope->iff : NULL), name);

    /* See if we are instantiating a template class. */
    if (type->atype == template_type)
    {
        classTmplDef *tcd;
        templateDef *td = type->u.td;

        for (tcd = pt->classtemplates; tcd != NULL; tcd = tcd->next)
            if (foundInScope(tcd->cd->iff->fqcname, td->fqname) &&
                sameTemplateSignature(&tcd->sig, &td->types, FALSE))
            {
                instantiateClassTemplate(pt, mod, scope, fqname, tcd, td,
                        getPythonName(mod, optflgs, name));

                /* All done. */
                return;
            }
    }

    td = sipMalloc(sizeof (typedefDef));

    td->tdflags = 0;
    td->fqname = fqname;
    td->ecd = scope;
    td->module = mod;
    td->type = *type;

    if (getOptFlag(optflgs, "Capsule", bool_flag) != NULL)
    {
        /* Make sure the type is void *. */
        if (type->atype != void_type || type->nrderefs != 1 || isConstArg(type) || isReference(type))
        {
            fatalScopedName(fqname);
            fatal(" must be a void* if /Capsule/ is specified\n");
        }

        td->type.atype = capsule_type;
        td->type.nrderefs = 0;
        td->type.u.cap = fqname;
    }

    if (getOptFlag(optflgs, "NoTypeName", bool_flag) != NULL)
        setNoTypeName(td);

    addTypedef(pt, td);
}


/*
 * Add a typedef to the list so that the list remains sorted.
 */
static void addTypedef(sipSpec *pt, typedefDef *tdd)
{
    typedefDef **tdp;

    /*
     * Check it doesn't already exist and find the position in the sorted list
     * where it should be put.
     */
    for (tdp = &pt->typedefs; *tdp != NULL; tdp = &(*tdp)->next)
    {
        int res = compareScopedNames((*tdp)->fqname, tdd->fqname);

        if (res == 0)
        {
            fatalScopedName(tdd->fqname);
            fatal(" already defined\n");
        }

        if (res > 0)
            break;
    }

    tdd->next = *tdp;
    *tdp = tdd;

    tdd->module->nrtypedefs++;
}


/*
 * Speculatively try and resolve any typedefs.  In some cases (eg. when
 * comparing template signatures) it helps to use the real type if it is known.
 * Note that this wouldn't be necessary if we required that all types be known
 * before they are used.
 */
static void resolveAnyTypedef(sipSpec *pt, argDef *ad)
{
    argDef orig = *ad;

    while (ad->atype == defined_type)
    {
        ad->atype = no_type;
        searchTypedefs(pt, ad->u.snd, ad);

        /*
         * Don't resolve to a template type as it may be superceded later on
         * by a more specific mapped type.
         */
        if (ad->atype == no_type || ad->atype == template_type)
        {
            *ad = orig;
            break;
        }
    }
}


/*
 * Return TRUE if the template signatures are the same.  A deep comparison is
 * used for mapped type templates where we want to recurse into any nested
 * templates.
 */
int sameTemplateSignature(signatureDef *tmpl_sd, signatureDef *args_sd,
        int deep)
{
    int a;

    if (tmpl_sd->nrArgs != args_sd->nrArgs)
        return FALSE;

    for (a = 0; a < tmpl_sd->nrArgs; ++a)
    {
        argDef *tmpl_ad = &tmpl_sd->args[a];
        argDef *args_ad = &args_sd->args[a];

        /*
         * If we are doing a shallow comparision (ie. for class templates) then
         * a type name in the template signature matches anything in the
         * argument signature.
         */
        if (tmpl_ad->atype == defined_type && !deep)
            continue;

        /*
         * For type names only compare the references and pointers, and do the
         * same for any nested templates.
         */
        if (tmpl_ad->atype == defined_type && args_ad->atype == defined_type)
        {
            if (isReference(tmpl_ad) != isReference(args_ad) || tmpl_ad->nrderefs != args_ad->nrderefs)
                return FALSE;
        }
        else if (tmpl_ad->atype == template_type && args_ad->atype == template_type)
        {
            if (!sameTemplateSignature(&tmpl_ad->u.td->types, &args_ad->u.td->types, deep))
                return FALSE;
        }
        else if (!sameBaseType(tmpl_ad, args_ad))
            return FALSE;
    }

    return TRUE;
}


/*
 * Create a new variable.
 */
static void newVar(sipSpec *pt, moduleDef *mod, char *name, int isstatic,
        argDef *type, optFlags *of, codeBlock *acode, codeBlock *gcode,
        codeBlock *scode, int section)
{
    varDef *var;
    classDef *escope = currentScope();
    nameDef *nd;

    /*
     * For the moment we don't support capsule variables because it needs the
     * API major version increasing.
     */
    if (type->atype == capsule_type)
        yyerror("Capsule variables not yet supported");

    /* Check the section. */
    if (section != 0)
    {
        if ((section & SECT_IS_PUBLIC) == 0)
            yyerror("Class variables must be in the public section");

        if (!isstatic && acode != NULL)
            yyerror("%AccessCode cannot be specified for non-static class variables");
    }

    if (isstatic && pt->genc)
        yyerror("Cannot have static members in a C structure");

    if (gcode != NULL || scode != NULL)
    {
        if (acode != NULL)
            yyerror("Cannot mix %AccessCode and %GetCode or %SetCode");

        if (escope == NULL)
            yyerror("Cannot specify %GetCode or %SetCode for global variables");
    }

    applyTypeFlags(mod, type, of);

    nd = cacheName(pt, getPythonName(mod, of, name));

    if (inMainModule())
        setIsUsedName(nd);

    checkAttributes(pt, mod, escope, NULL, nd->text, FALSE);

    var = sipMalloc(sizeof (varDef));

    var->pyname = nd;
    var->fqcname = text2scopedName((escope != NULL ? escope->iff : NULL),
            name);
    var->ecd = escope;
    var->module = mod;
    var->varflags = 0;
    var->no_typehint = getNoTypeHint(of);
    var->type = *type;
    appendCodeBlock(&var->accessfunc, acode);
    appendCodeBlock(&var->getcode, gcode);
    appendCodeBlock(&var->setcode, scode);

    if (isstatic || (escope != NULL && escope->iff->type == namespace_iface))
        setIsStaticVar(var);

    if (getOptFlag(of, "NoSetter", bool_flag) != NULL)
        setNoSetter(var);

    addVariable(pt, var);
}


/*
 * Create a new ctor.
 */
static void newCtor(moduleDef *mod, char *name, int sectFlags,
        signatureDef *args, optFlags *optflgs, codeBlock *methodcode,
        throwArgs *exceptions, signatureDef *cppsig, int explicit,
        codeBlock *docstring)
{
    ctorDef *ct, **ctp;
    classDef *cd = currentScope();

    /* Check the name of the constructor. */
    if (strcmp(classBaseName(cd), name) != 0)
        yyerror("Constructor doesn't have the same name as its class");

    if (docstring != NULL)
        appendCodeBlock(&cd->docstring, docstring);

    /* Add to the list of constructors. */
    ct = sipMalloc(sizeof (ctorDef));

    if (sectFlags & SECT_IS_PROT && makeProtPublic)
    {
        sectFlags &= ~SECT_IS_PROT;
        sectFlags |= SECT_IS_PUBLIC;
    }

    /* Allow the signature to be used like an function signature. */
    memset(&args->result, 0, sizeof (argDef));
    args->result.atype = void_type;

    ct->ctorflags = sectFlags;
    ct->no_typehint = getNoTypeHint(optflgs);
    ct->api_range = getAPIRange(optflgs);
    ct->pysig = *args;
    ct->cppsig = (cppsig != NULL ? cppsig : &ct->pysig);
    ct->exceptions = exceptions;
    appendCodeBlock(&ct->methodcode, methodcode);

    if (!isPrivateCtor(ct))
        setCanCreate(cd);

    if (isProtectedCtor(ct))
        setHasShadow(cd);

    if (explicit)
        setIsExplicitCtor(ct);

    getHooks(optflgs, &ct->prehook, &ct->posthook);

    if (getReleaseGIL(optflgs))
        setIsReleaseGILCtor(ct);
    else if (getHoldGIL(optflgs))
        setIsHoldGILCtor(ct);

    if (getTransfer(optflgs))
        setIsResultTransferredCtor(ct);

    if (getDeprecated(optflgs))
        setIsDeprecatedCtor(ct);

    if (!isPrivateCtor(ct))
        ct->kwargs = keywordArgs(mod, optflgs, &ct->pysig, FALSE);

    if (methodcode == NULL && getOptFlag(optflgs, "NoRaisesPyException", bool_flag) == NULL)
    {
        if (allRaisePyException(mod) || getOptFlag(optflgs, "RaisesPyException", bool_flag) != NULL)
            setRaisesPyExceptionCtor(ct);
    }

    if (getOptFlag(optflgs, "NoDerived", bool_flag) != NULL)
    {
        if (cppsig != NULL)
            yyerror("The /NoDerived/ annotation cannot be used with a C++ signature");

        if (methodcode == NULL)
            yyerror("The /NoDerived/ annotation must be used with %MethodCode");

        ct->cppsig = NULL;
    }

    if (getOptFlag(optflgs, "Default", bool_flag) != NULL)
    {
        if (cd->defctor != NULL)
            yyerror("A constructor with the /Default/ annotation has already been defined");

        cd->defctor = ct;
    }

    /* Append to the list. */
    for (ctp = &cd->ctors; *ctp != NULL; ctp = &(*ctp)->next)
        ;

    *ctp = ct;
}


/*
 * Create a new function.
 */
static void newFunction(sipSpec *pt, moduleDef *mod, classDef *c_scope,
        mappedTypeDef *mt_scope, int sflags, int isstatic, int issignal,
        int isslot, int isvirt, char *name, signatureDef *sig, int isconst,
        int isabstract, optFlags *optflgs, codeBlock *methodcode,
        codeBlock *vcode, codeBlock *virtcallcode, throwArgs *exceptions,
        signatureDef *cppsig, codeBlock *docstring)
{
    static const char *annos[] = {
        "__len__",
        "__imatmul__",
        "__matmul__",
        "AbortOnException",
        "AllowNone",
        "API",
        "AutoGen",
        "Deprecated",
        "DisallowNone",
        "DocType",
        "Encoding",
        "Factory",
        "HoldGIL",
        "KeywordArgs",
        "KeepReference",
        "NewThread",
        "NoArgParser",
        "NoCopy",
        "NoRaisesPyException",
        "NoTypeHint",
        "NoVirtualErrorHandler",
        "Numeric",
        "PostHook",
        "PreHook",
        "PyInt",
        "PyName",
        "PyQtSignalHack",
        "RaisesPyException",
        "ReleaseGIL",
        "Sequence",
        "VirtualErrorHandler",
        "Transfer",
        "TransferBack",
        "TransferThis",
        "TypeHint",
        NULL
    };

    const char *pyname, *virt_error_handler;
    int factory, xferback, no_arg_parser, no_virt_error_handler;
    overDef *od, **odp, **headp;
    optFlag *of;
    virtHandlerDef *vhd;

    checkAnnos(optflgs, annos);

    /* Extra checks for a C module. */
    if (pt->genc)
    {
        if (c_scope != NULL)
            yyerror("Function declaration not allowed in a struct in a C module");

        if (isstatic)
            yyerror("Static functions not allowed in a C module");

        if (exceptions != NULL)
            yyerror("Exceptions not allowed in a C module");

        /* Handle C void prototypes. */
        if (sig->nrArgs == 1)
        {
            argDef *vad = &sig->args[0];

            if (vad->atype == void_type && vad->nrderefs == 0)
                sig->nrArgs = 0;
        }
    }

    if (mt_scope != NULL)
        headp = &mt_scope->overs;
    else if (c_scope != NULL)
        headp = &c_scope->overs;
    else
        headp = &mod->overs;

    /*
     * See if the function has a non-lazy method.  These are methods that
     * Python expects to see defined in the type before any instance of the
     * type is created.
     */
    if (c_scope != NULL)
    {
        static const char *lazy[] = {
            "__getattribute__",
            "__getattr__",
            "__enter__",
            "__exit__",
            "__aenter__",
            "__aexit__",
            NULL
        };

        const char **l;

        for (l = lazy; *l != NULL; ++l)
            if (strcmp(name, *l) == 0)
            {
                setHasNonlazyMethod(c_scope);
                break;
            }
    }

    /* See if it is a factory method. */
    if (getOptFlag(optflgs, "Factory", bool_flag) != NULL)
        factory = TRUE;
    else
    {
        int a;

        factory = FALSE;

        /* Check /TransferThis/ wasn't specified. */
        if (c_scope == NULL || isstatic)
            for (a = 0; a < sig->nrArgs; ++a)
                if (isThisTransferred(&sig->args[a]))
                    yyerror("/TransferThis/ may only be specified in constructors and class methods");
    }

    /* See if the result is to be returned to Python ownership. */
    xferback = (getOptFlag(optflgs, "TransferBack", bool_flag) != NULL);

    if (factory && xferback)
        yyerror("/TransferBack/ and /Factory/ cannot both be specified");

    /* Create a new overload definition. */

    od = sipMalloc(sizeof (overDef));

    getSourceLocation(&od->sloc);

    /* Set the overload flags. */

    if ((sflags & SECT_IS_PROT) && makeProtPublic)
    {
        sflags &= ~SECT_IS_PROT;
        sflags |= SECT_IS_PUBLIC | OVER_REALLY_PROT;
    }

    od->overflags = sflags;

    if (issignal)
    {
        resetIsSlot(od);
        setIsSignal(od);
    }
    else if (isslot)
    {
        resetIsSignal(od);
        setIsSlot(od);
    }

    od->no_typehint = getNoTypeHint(optflgs);

    if (isSignal(od))
        if ((of = getOptFlag(optflgs, "PyQtSignalHack", integer_flag)) != NULL)
            od->pyqt_signal_hack = of->fvalue.ival;

    if (factory)
        setIsFactory(od);

    if (xferback)
        setIsResultTransferredBack(od);

    if (getTransfer(optflgs))
        setIsResultTransferred(od);

    if (getOptFlag(optflgs, "TransferThis", bool_flag) != NULL)
        setIsThisTransferredMeth(od);

    if (methodcode == NULL && getOptFlag(optflgs, "NoRaisesPyException", bool_flag) == NULL)
    {
        if (allRaisePyException(mod) || getOptFlag(optflgs, "RaisesPyException", bool_flag) != NULL)
            setRaisesPyException(od);
    }

    if (isProtected(od))
        setHasShadow(c_scope);

    if ((isSlot(od) || isSignal(od)) && !isPrivate(od))
    {
        if (isSignal(od))
            setHasShadow(c_scope);

        pt->sigslots = TRUE;
    }

    if (isSignal(od) && (methodcode != NULL || vcode != NULL || virtcallcode != NULL))
        yyerror("Cannot provide code for signals");

    if (isstatic)
    {
        if (isSignal(od))
            yyerror("Static functions cannot be signals");

        if (isvirt)
            yyerror("Static functions cannot be virtual");

        setIsStatic(od);
    }

    if (isconst)
        setIsConst(od);

    if (isabstract)
    {
        if (sflags == 0)
            yyerror("Non-class function specified as abstract");

        setIsAbstract(od);
    }

    if ((of = getOptFlag(optflgs, "AutoGen", opt_name_flag)) != NULL)
    {
        if (of->fvalue.sval == NULL || isEnabledFeature(of->fvalue.sval))
            setIsAutoGen(od);
    }

    virt_error_handler = getVirtErrorHandler(optflgs);
    no_virt_error_handler = (getOptFlag(optflgs, "NoVirtualErrorHandler", bool_flag) != NULL);

    if (isvirt)
    {
        if (isSignal(od) && pluginPyQt3(pt))
            yyerror("Virtual signals aren't supported");

        setIsVirtual(od);
        setHasShadow(c_scope);

        vhd = sipMalloc(sizeof (virtHandlerDef));

        vhd->virthandlernr = -1;
        vhd->vhflags = 0;
        vhd->pysig = &od->pysig;
        vhd->cppsig = (cppsig != NULL ? cppsig : &od->pysig);
        appendCodeBlock(&vhd->virtcode, vcode);

        if (factory || xferback)
            setIsTransferVH(vhd);

        if (getOptFlag(optflgs, "AbortOnException", bool_flag) != NULL)
            setAbortOnException(vhd);

        if (no_virt_error_handler)
        {
            if (virt_error_handler != NULL)
                yyerror("/VirtualErrorHandler/ and /NoVirtualErrorHandler/ provided");

            setNoErrorHandler(od);
        }
        else
        {
            od->virt_error_handler = virt_error_handler;
        }

        /*
         * Only add it to the module's virtual handlers if we are not in a
         * class template.
         */
        if (!currentIsTemplate)
        {
            vhd->module = mod;

            vhd->next = mod->virthandlers;
            mod->virthandlers = vhd;
        }
    }
    else
    {
        if (vcode != NULL)
            yyerror("%VirtualCatcherCode provided for non-virtual function");

        if (virt_error_handler != NULL)
            yyerror("/VirtualErrorHandler/ provided for non-virtual function");

        if (no_virt_error_handler)
            yyerror("/NoVirtualErrorHandler/ provided for non-virtual function");

        vhd = NULL;
    }

    od->cppname = name;
    od->pysig = *sig;
    od->cppsig = (cppsig != NULL ? cppsig : &od->pysig);
    od->exceptions = exceptions;
    appendCodeBlock(&od->methodcode, methodcode);
    appendCodeBlock(&od->virtcallcode, virtcallcode);
    od->virthandler = vhd;

    no_arg_parser = (getOptFlag(optflgs, "NoArgParser", bool_flag) != NULL);

    if (no_arg_parser)
    {
        if (methodcode == NULL)
            yyerror("%MethodCode must be supplied if /NoArgParser/ is specified");
    }
    else
    {
        /*
         * The argument parser requires that there is nothing after an
         * ellipsis.
         */
        checkEllipsis(sig);
    }

    if (cppsig != NULL)
        checkEllipsis(cppsig);

    if (getOptFlag(optflgs, "NoCopy", bool_flag) != NULL)
        setNoCopy(&od->pysig.result);

    if (getAllowNone(optflgs))
        setAllowNone(&od->pysig.result);

    if (getDisallowNone(optflgs))
        setDisallowNone(&od->pysig.result);

    handleKeepReference(optflgs, &od->pysig.result, mod);

    pyname = getPythonName(mod, optflgs, name);

    od->common = findFunction(pt, mod, c_scope, mt_scope, pyname,
            (methodcode != NULL), sig->nrArgs, no_arg_parser);

    if (isProtected(od))
        setHasProtected(od->common);

    if (strcmp(pyname, "__delattr__") == 0)
        setIsDelattr(od);

    if (docstring != NULL)
        appendCodeBlock(&od->common->docstring, docstring);

    od->api_range = getAPIRange(optflgs);

    if (od->api_range == NULL)
        setNotVersioned(od->common);

    if (getOptFlag(optflgs, "Numeric", bool_flag) != NULL)
    {
        if (isSequence(od->common))
            yyerror("/Sequence/ has already been specified");

        setIsNumeric(od->common);
    }

    if (getOptFlag(optflgs, "Sequence", bool_flag) != NULL)
    {
        if (isNumeric(od->common))
            yyerror("/Numeric/ has already been specified");

        setIsSequence(od->common);
    }

    /* Methods that run in new threads must be virtual. */
    if (getOptFlag(optflgs, "NewThread", bool_flag) != NULL)
    {
        argDef *res;

        if (!isvirt)
            yyerror("/NewThread/ may only be specified for virtual functions");

        /*
         * This is an arbitary limitation to make the code generator slightly
         * easier - laziness on my part.
         */
        res = &od->cppsig->result;

        if (res->atype != void_type || res->nrderefs != 0)
            yyerror("/NewThread/ may only be specified for void functions");

        setIsNewThread(od);
    }

    getHooks(optflgs, &od->prehook, &od->posthook);

    if (getReleaseGIL(optflgs))
        setIsReleaseGIL(od);
    else if (getHoldGIL(optflgs))
        setIsHoldGIL(od);

    if (getDeprecated(optflgs))
        setIsDeprecated(od);

    if (!isPrivate(od) && !isSignal(od) && (od->common->slot == no_slot || od->common->slot == call_slot))
    {
        od->kwargs = keywordArgs(mod, optflgs, &od->pysig, hasProtected(od->common));

        if (od->kwargs != NoKwArgs)
            setUseKeywordArgs(od->common);

        /*
         * If the overload is protected and defined in an imported module then
         * we need to make sure that any other overloads' keyword argument
         * names are marked as used.
         */
        if (isProtected(od) && !inMainModule())
        {
            overDef *kwod;

            for (kwod = c_scope->overs; kwod != NULL; kwod = kwod->next)
                if (kwod->common == od->common && kwod->kwargs != NoKwArgs)
                {
                    int a;

                    for (a = 0; a < kwod->pysig.nrArgs; ++a)
                    {
                        argDef *ad = &kwod->pysig.args[a];

                        if (kwod->kwargs == OptionalKwArgs && ad->defval == NULL)
                            continue;

                        if (ad->name != NULL)
                            setIsUsedName(ad->name);
                    }
                }
        }
    }

    od->next = NULL;

    /* See if we want to auto-generate some methods. */
    if (getOptFlag(optflgs, "__len__", bool_flag) != NULL)
    {
        overDef *len;

        len = sipMalloc(sizeof (overDef));

        len->cppname = "__len__";
        len->overflags = SECT_IS_PUBLIC;
        len->pysig.result.atype = ssize_type;
        len->pysig.nrArgs = 0;
        len->cppsig = &len->pysig;

        if ((len->methodcode = od->methodcode) == NULL)
        {
            char *buf = sipStrdup("            sipRes = (SIP_SSIZE_T)sipCpp->");
            codeBlock *code;

            append(&buf, od->cppname);
            append(&buf, "();\n");

            code = sipMalloc(sizeof (codeBlock));

            code->frag = buf;
            code->filename = "Auto-generated";
            code->linenr = 1;

            appendCodeBlock(&len->methodcode, code);
        }

        len->common = findFunction(pt, mod, c_scope, mt_scope, len->cppname,
                TRUE, 0, FALSE);

        len->next = od->next;
        od->next = len;
    }

    if (getOptFlag(optflgs, "__matmul__", bool_flag) != NULL)
    {
        overDef *matmul;

        matmul = sipMalloc(sizeof (overDef));

        matmul->cppname = "__matmul__";
        matmul->overflags = SECT_IS_PUBLIC;
        matmul->pysig = od->pysig;
        matmul->cppsig = (cppsig != NULL ? cppsig : &matmul->pysig);

        matmul->methodcode = od->methodcode;

        matmul->common = findFunction(pt, mod, c_scope, mt_scope,
                matmul->cppname, (matmul->methodcode != NULL),
                matmul->pysig.nrArgs, FALSE);

        matmul->next = od->next;
        od->next = matmul;
    }

    if (getOptFlag(optflgs, "__imatmul__", bool_flag) != NULL)
    {
        overDef *imatmul;

        imatmul = sipMalloc(sizeof (overDef));

        imatmul->cppname = "__imatmul__";
        imatmul->overflags = SECT_IS_PUBLIC;
        imatmul->pysig = od->pysig;
        imatmul->cppsig = (cppsig != NULL ? cppsig : &imatmul->pysig);

        imatmul->methodcode = od->methodcode;

        imatmul->common = findFunction(pt, mod, c_scope, mt_scope,
                imatmul->cppname, (imatmul->methodcode != NULL),
                imatmul->pysig.nrArgs, FALSE);

        imatmul->next = od->next;
        od->next = imatmul;
    }

    /* Append to the list. */
    for (odp = headp; *odp != NULL; odp = &(*odp)->next)
        ;

    *odp = od;
}


/*
 * Return the Python name based on the C/C++ name and any /PyName/ annotation.
 */
static const char *getPythonName(moduleDef *mod, optFlags *optflgs,
        const char *cname)
{
    const char *pname;
    optFlag *of;
    autoPyNameDef *apnd;

    /* Use the explicit name if given. */
    if ((of = getOptFlag(optflgs, "PyName", name_flag)) != NULL)
        return of->fvalue.sval;

    /* Apply any automatic naming rules. */
    pname = cname;

    for (apnd = mod->autopyname; apnd != NULL; apnd = apnd->next)
    {
        size_t len = strlen(apnd->remove_leading);

        if (strncmp(pname, apnd->remove_leading, len) == 0)
            pname += len;
    }

    return pname;
}


/*
 * Cache a name in a module.  Entries in the cache are stored in order of
 * decreasing length.
 */
nameDef *cacheName(sipSpec *pt, const char *name)
{
    nameDef *nd, **ndp;
    size_t len;

    /* Allow callers to be lazy about checking if there is really a name. */
    if (name == NULL)
        return NULL;

    /* Skip entries that are too large. */
    ndp = &pt->namecache;
    len = strlen(name);

    while (*ndp != NULL && (*ndp)->len > len)
        ndp = &(*ndp)->next;

    /* Check entries that are the right length. */
    for (nd = *ndp; nd != NULL && nd->len == len; nd = nd->next)
        if (memcmp(nd->text, name, len) == 0)
            return nd;

    /* Create a new one. */
    nd = sipMalloc(sizeof (nameDef));

    nd->nameflags = 0;
    nd->text = name;
    nd->len = len;
    nd->next = *ndp;

    *ndp = nd;

    return nd;
}


/*
 * Find (or create) an overloaded function name.
 */
static memberDef *findFunction(sipSpec *pt, moduleDef *mod, classDef *c_scope,
        mappedTypeDef *mt_scope, const char *pname, int hwcode, int nrargs,
        int no_arg_parser)
{
    static struct slot_map {
        const char *name;   /* The slot name. */
        slotType type;      /* The corresponding type. */
        int needs_hwcode;   /* Set if handwritten code is required. */
        int nrargs;         /* Nr. of arguments. */
    } slot_table[] = {
        {"__str__", str_slot, TRUE, 0},
        {"__int__", int_slot, FALSE, 0},
        {"__long__", long_slot, FALSE, 0},
        {"__float__", float_slot, FALSE, 0},
        {"__len__", len_slot, TRUE, 0},
        {"__contains__", contains_slot, TRUE, 1},
        {"__add__", add_slot, FALSE, 1},
        {"__sub__", sub_slot, FALSE, 1},
        {"__mul__", mul_slot, FALSE, 1},
        {"__div__", div_slot, FALSE, 1},
        {"__mod__", mod_slot, FALSE, 1},
        {"__floordiv__", floordiv_slot, TRUE, 1},
        {"__truediv__", truediv_slot, FALSE, 1},
        {"__and__", and_slot, FALSE, 1},
        {"__or__", or_slot, FALSE, 1},
        {"__xor__", xor_slot, FALSE, 1},
        {"__lshift__", lshift_slot, FALSE, 1},
        {"__rshift__", rshift_slot, FALSE, 1},
        {"__iadd__", iadd_slot, FALSE, 1},
        {"__isub__", isub_slot, FALSE, 1},
        {"__imul__", imul_slot, FALSE, 1},
        {"__idiv__", idiv_slot, FALSE, 1},
        {"__imod__", imod_slot, FALSE, 1},
        {"__ifloordiv__", ifloordiv_slot, TRUE, 1},
        {"__itruediv__", itruediv_slot, FALSE, 1},
        {"__iand__", iand_slot, FALSE, 1},
        {"__ior__", ior_slot, FALSE, 1},
        {"__ixor__", ixor_slot, FALSE, 1},
        {"__ilshift__", ilshift_slot, FALSE, 1},
        {"__irshift__", irshift_slot, FALSE, 1},
        {"__invert__", invert_slot, FALSE, 0},
        {"__call__", call_slot, FALSE, -1},
        {"__getitem__", getitem_slot, FALSE, 1},
        {"__setitem__", setitem_slot, TRUE, 2},
        {"__delitem__", delitem_slot, TRUE, 1},
        {"__lt__", lt_slot, FALSE, 1},
        {"__le__", le_slot, FALSE, 1},
        {"__eq__", eq_slot, FALSE, 1},
        {"__ne__", ne_slot, FALSE, 1},
        {"__gt__", gt_slot, FALSE, 1},
        {"__ge__", ge_slot, FALSE, 1},
        {"__cmp__", cmp_slot, FALSE, 1},
        {"__bool__", bool_slot, TRUE, 0},
        {"__nonzero__", bool_slot, TRUE, 0},
        {"__neg__", neg_slot, FALSE, 0},
        {"__pos__", pos_slot, FALSE, 0},
        {"__abs__", abs_slot, TRUE, 0},
        {"__repr__", repr_slot, TRUE, 0},
        {"__hash__", hash_slot, TRUE, 0},
        {"__index__", index_slot, TRUE, 0},
        {"__iter__", iter_slot, TRUE, 0},
        {"__next__", next_slot, TRUE, 0},
        {"__setattr__", setattr_slot, TRUE, 2},
        {"__delattr__", delattr_slot, TRUE, 1},
        {"__matmul__", matmul_slot, FALSE, 1},
        {"__imatmul__", imatmul_slot, FALSE, 1},
        {"__await__", await_slot, TRUE, 0},
        {"__aiter__", aiter_slot, TRUE, 0},
        {"__anext__", anext_slot, TRUE, 0},
        {NULL, no_slot, FALSE, 0}
    };

    memberDef *md, **flist;
    struct slot_map *sm;
    slotType st;

    /* Get the slot type. */
    st = no_slot;

    for (sm = slot_table; sm->name != NULL; ++sm)
        if (strcmp(sm->name, pname) == 0)
        {
            if (sm->needs_hwcode && !hwcode)
                yyerror("This Python slot requires %MethodCode");

            if (sm->nrargs >= 0)
            {
                if (mt_scope == NULL && c_scope == NULL)
                {
                    /* Global operators need one extra argument. */
                    if (sm -> nrargs + 1 != nrargs)
                        yyerror("Incorrect number of arguments to global operator");
                }
                else if (sm->nrargs != nrargs)
                    yyerror("Incorrect number of arguments to Python slot");
            }

            st = sm->type;

            break;
        }

    /* Check there is no name clash. */
    checkAttributes(pt, mod, c_scope, mt_scope, pname, TRUE);

    /* See if it already exists. */
    if (mt_scope != NULL)
        flist = &mt_scope->members;
    else if (c_scope != NULL)
        flist = &c_scope->members;
    else
        flist = &mod->othfuncs;

    /* __delattr__ is implemented as __setattr__. */
    if (st == delattr_slot)
    {
        if (inMainModule())
            setIsUsedName(cacheName(pt, pname));

        st = setattr_slot;
        pname = "__setattr__";
    }

    for (md = *flist; md != NULL; md = md->next)
        if (strcmp(md->pyname->text, pname) == 0 && md->module == mod)
            break;

    if (md == NULL)
    {
        /* Create a new one. */
        md = sipMalloc(sizeof (memberDef));

        md->pyname = cacheName(pt, pname);
        md->memberflags = 0;
        md->slot = st;
        md->module = mod;
        md->next = *flist;

        *flist = md;

        if (inMainModule())
            setIsUsedName(md->pyname);

        if (no_arg_parser)
            setNoArgParser(md);
    }
    else if (noArgParser(md))
        yyerror("Another overload has already been defined that is annotated as /NoArgParser/");

    /* Global operators are a subset. */
    if (mt_scope == NULL && c_scope == NULL && st != no_slot && st != neg_slot && st != pos_slot && !isNumberSlot(md) && !isInplaceNumberSlot(md) && !isRichCompareSlot(md))
        yyerror("Global operators must be either numeric or comparison operators");

    return md;
}


/*
 * Search a set of flags for a particular one.
 */
static optFlag *findOptFlag(optFlags *flgs, const char *name)
{
    int f;

    for (f = 0; f < flgs->nrFlags; ++f)
    {
        optFlag *of = &flgs->flags[f];

        if (strcmp(of->fname, name) == 0)
            return of;
    }

    return NULL;
}


/*
 * Search a set of flags for a particular one and check its type.
 */
static optFlag *getOptFlag(optFlags *flgs, const char *name, flagType ft)
{
    optFlag *of = findOptFlag(flgs, name);

    if (of != NULL)
    {
        /* An optional name can look like a boolean or a name. */
        if (ft == opt_name_flag)
        {
            if (of->ftype == bool_flag)
            {
                of->ftype = opt_name_flag;
                of->fvalue.sval = NULL;
            }
            else if (of->ftype == name_flag)
            {
                of->ftype = opt_name_flag;
            }
        }

        /* An optional integer can look like a boolean or an integer. */
        if (ft == opt_integer_flag)
        {
            if (of->ftype == bool_flag)
            {
                of->ftype = opt_integer_flag;
                of->fvalue.ival = -1;
            }
            else if (of->ftype == integer_flag)
            {
                of->ftype = opt_integer_flag;
            }
        }

        if (ft != of->ftype)
            yyerror("Annotation has a value of the wrong type");
    }

    return of;
}


/*
 * A name is going to be used as a Python attribute name within a Python scope
 * (ie. a Python dictionary), so check against what we already know is going in
 * the same scope in case there is a clash.
 */
static void checkAttributes(sipSpec *pt, moduleDef *mod, classDef *py_c_scope,
        mappedTypeDef *py_mt_scope, const char *attr, int isfunc)
{
    enumDef *ed;
    varDef *vd;
    classDef *cd;

    /* Check the enums. */

    for (ed = pt->enums; ed != NULL; ed = ed->next)
    {
        enumMemberDef *emd;

        if (ed->pyname == NULL)
            continue;

        if (py_c_scope != NULL)
        {
            if (ed->ecd != py_c_scope)
                continue;
        }
        else if (py_mt_scope != NULL)
        {
            if (ed->emtd != py_mt_scope)
                continue;
        }
        else if (ed->ecd != NULL || ed->emtd != NULL)
        {
            continue;
        }

        if (strcmp(ed->pyname->text, attr) == 0)
            yyerror("There is already an enum in scope with the same Python name");

        for (emd = ed->members; emd != NULL; emd = emd->next)
            if (strcmp(emd->pyname->text, attr) == 0)
                yyerror("There is already an enum member in scope with the same Python name");
    }

    /*
     * Only check the members if this attribute isn't a member because we
     * can handle members with the same name in the same scope.
     */
    if (!isfunc)
    {
        memberDef *md, *membs;
        overDef *overs;

        if (py_mt_scope != NULL)
        {
            membs = py_mt_scope->members;
            overs = py_mt_scope->overs;
        }
        else if (py_c_scope != NULL)
        {
            membs = py_c_scope->members;
            overs = py_c_scope->overs;
        }
        else
        {
            membs = mod->othfuncs;
            overs = mod->overs;
        }

        for (md = membs; md != NULL; md = md->next)
        {
            overDef *od;

            if (strcmp(md->pyname->text, attr) != 0)
                continue;

            /* Check for a conflict with all overloads. */
            for (od = overs; od != NULL; od = od->next)
            {
                if (od->common != md)
                    continue;

                yyerror("There is already a function in scope with the same Python name");
            }
        }
    }

    /* If the scope was a mapped type then that's all we have to check. */
    if (py_mt_scope != NULL)
        return;

    /* Check the variables. */
    for (vd = pt->vars; vd != NULL; vd = vd->next)
    {
        if (vd->ecd != py_c_scope)
            continue;

        if (strcmp(vd->pyname->text,attr) == 0)
            yyerror("There is already a variable in scope with the same Python name");
    }

    /* Check the classes. */
    for (cd = pt->classes; cd != NULL; cd = cd->next)
    {
        if (cd->ecd != py_c_scope || cd->pyname == NULL)
            continue;

        if (strcmp(cd->pyname->text, attr) == 0 && !isExternal(cd))
            yyerror("There is already a class or namespace in scope with the same Python name");
    }

    /* Check the exceptions. */
    if (py_c_scope == NULL)
    {
        exceptionDef *xd;

        for (xd = pt->exceptions; xd != NULL; xd = xd->next)
            if (xd->pyname != NULL && strcmp(xd->pyname, attr) == 0)
                yyerror("There is already an exception with the same Python name");
    }

    /* Check the properties. */
    if (py_c_scope != NULL)
    {
        propertyDef *pd;

        for (pd = py_c_scope->properties; pd != NULL; pd = pd->next)
            if (strcmp(pd->name->text, attr) == 0)
                yyerror("There is already a property with the same name");
    }
}


/*
 * Append a code block to a list of them.
 */
static void appendCodeBlock(codeBlockList **headp, codeBlock *cb)
{
    codeBlockList *cbl;

    /* Handle the trivial case. */
    if (cb == NULL)
        return;

    /* Find the end of the list. */
    while (*headp != NULL)
    {
        /* Ignore if the block is already in the list. */
        if ((*headp)->block == cb)
            return;

        headp = &(*headp)->next;
    }

    cbl = sipMalloc(sizeof (codeBlockList));
    cbl->block = cb;

    *headp = cbl;
}


/*
 * Append a code block list to an existing list.
 */
void appendCodeBlockList(codeBlockList **headp, codeBlockList *cbl)
{
    while (cbl != NULL)
    {
        appendCodeBlock(headp, cbl->block);
        cbl = cbl->next;
    }
}


/*
 * Handle the end of a fully parsed a file.
 */
static void handleEOF()
{
    /*
     * Check that the number of nested if's is the same as when we started
     * the file.
     */

    if (skipStackPtr > currentContext.ifdepth)
        fatal("Too many %%If statements in %s\n", previousFile);

    if (skipStackPtr < currentContext.ifdepth)
        fatal("Too many %%End statements in %s\n", previousFile);
}


/*
 * Handle the end of a fully parsed a module.
 */
static void handleEOM()
{
    moduleDef *from;

    /* Check it has been named. */
    if (currentModule->name == NULL)
        fatal("No %%Module has been specified for module defined in %s\n",
                previousFile);

    from = currentContext.prevmod;

    if (from != NULL)
    {
        if (from->encoding == no_type)
            from->encoding = currentModule->encoding;

        if (isCallSuperInitUndefined(from))
        {
            if (isCallSuperInitYes(currentModule))
                setCallSuperInitYes(from);
            else
                setCallSuperInitNo(from);
        }
    }

    /* The previous module is now current. */
    currentModule = from;
}


/*
 * Find an existing qualifier.
 */
static qualDef *findQualifier(const char *name)
{
    moduleDef *mod;

    for (mod = currentSpec->modules; mod != NULL; mod = mod->next)
    {
        qualDef *qd;

        for (qd = mod->qualifiers; qd != NULL; qd = qd->next)
            if (strcmp(qd->name, name) == 0)
                return qd;
    }

    /* Qualifiers corresponding to the SIP version are created on the fly. */
    if (name[0] == 'S' && name[1] == 'I' && name[2] == 'P' && name[3] == '_')
    {
        const char *cp = &name[3];
        int major, minor, patch;

        cp = getInt(cp, &major);
        cp = getInt(cp, &minor);
        cp = getInt(cp, &patch);

        if (*cp != '\0')
            yyerror("Unexpected character after SIP version number");

        return allocQualifier(currentModule, -1,
                (major << 16) | (minor << 8) | patch, TRUE, name,
                time_qualifier);
    }

    return NULL;
}


/*
 * Get an integer from string.
 */
static const char *getInt(const char *cp, int *ip)
{
    /* Handle the default value. */
    *ip = 0;

    if (*cp == '\0')
        return cp;

    /* There must be a leading underscore. */
    if (*cp++ != '_')
        yyerror("An underscore must separate the parts of a SIP version number");

    while (isdigit(*cp))
    {
        *ip *= 10;
        *ip += *cp - '0';
        ++cp;
    }

    return cp;
}


/*
 * Find an existing API.
 */
apiVersionRangeDef *findAPI(sipSpec *pt, const char *name)
{
    moduleDef *mod;

    for (mod = pt->modules; mod != NULL; mod = mod->next)
    {
        apiVersionRangeDef *avd;

        for (avd = mod->api_versions; avd != NULL; avd = avd->next)
            if (strcmp(avd->api_name->text, name) == 0)
                return avd;
    }

    return NULL;
}


/*
 * Return a copy of a scoped name.
 */
scopedNameDef *copyScopedName(scopedNameDef *snd)
{
    scopedNameDef *head;

    head = NULL;

    while (snd != NULL)
    {
        appendScopedName(&head,text2scopePart(snd -> name));
        snd = snd -> next;
    }

    return head;
}


/*
 * Append a name to a list of scopes.
 */
void appendScopedName(scopedNameDef **headp,scopedNameDef *newsnd)
{
    while (*headp != NULL)
        headp = &(*headp) -> next;

    *headp = newsnd;
}


/*
 * Free a scoped name - but not the text itself.
 */
void freeScopedName(scopedNameDef *snd)
{
    while (snd != NULL)
    {
        scopedNameDef *next = snd -> next;

        free(snd);

        snd = next;
    }
}


/*
 * Convert a text string to a scope part structure.
 */
static scopedNameDef *text2scopePart(char *text)
{
    scopedNameDef *snd;

    snd = sipMalloc(sizeof (scopedNameDef));

    snd->name = text;
    snd->next = NULL;

    return snd;
}


/*
 * Convert a text string to a fully scoped name.
 */
static scopedNameDef *text2scopedName(ifaceFileDef *scope, char *text)
{
    return scopeScopedName(scope, text2scopePart(text));
}


/*
 * Prepend any current scope to a scoped name.
 */
static scopedNameDef *scopeScopedName(ifaceFileDef *scope, scopedNameDef *name)
{
    scopedNameDef *snd;

    snd = (scope != NULL ? copyScopedName(scope->fqcname) : NULL);

    appendScopedName(&snd, name);

    return snd;
}


/*
 * Return a pointer to the tail part of a scoped name.
 */
char *scopedNameTail(scopedNameDef *snd)
{
    if (snd == NULL)
        return NULL;

    while (snd -> next != NULL)
        snd = snd -> next;

    return snd -> name;
}


/*
 * Push the given scope onto the scope stack.
 */
static void pushScope(classDef *scope)
{
    if (currentScopeIdx >= MAX_NESTED_SCOPE)
        fatal("Internal error: increase the value of MAX_NESTED_SCOPE\n");

    scopeStack[currentScopeIdx] = scope;
    sectFlagsStack[currentScopeIdx] = sectionFlags;

    ++currentScopeIdx;
}


/*
 * Pop the scope stack.
 */
static void popScope(void)
{
    if (currentScopeIdx > 0)
        sectionFlags = sectFlagsStack[--currentScopeIdx];
}


/*
 * Return non-zero if the current input should be parsed rather than be
 * skipped.
 */
static int notSkipping()
{
    return (skipStackPtr == 0 ? TRUE : skipStack[skipStackPtr - 1]);
}


/*
 * Return the value of an expression involving a time period.
 */
static int timePeriod(const char *lname, const char *uname)
{
    int line;
    qualDef *qd, *lower, *upper;
    moduleDef *mod;

    if (lname == NULL)
        lower = NULL;
    else if ((lower = findQualifier(lname)) == NULL || lower->qtype != time_qualifier)
        yyerror("Lower bound is not a time version");

    if (uname == NULL)
        upper = NULL;
    else if ((upper = findQualifier(uname)) == NULL || upper->qtype != time_qualifier)
        yyerror("Upper bound is not a time version");

    /* Sanity checks on the bounds. */
    if (lower == NULL && upper == NULL)
        yyerror("Lower and upper bounds cannot both be omitted");

    if (lower != NULL && upper != NULL)
    {
        if (lower->module != upper->module || lower->line != upper->line)
            yyerror("Lower and upper bounds are from different timelines");

        if (lower == upper)
            yyerror("Lower and upper bounds must be different");

        if (lower->order > upper->order)
            yyerror("Later version specified as lower bound");
    }

    /* Go through each slot in the relevant timeline. */
    if (lower != NULL)
    {
        mod = lower->module;
        line = lower->line;
    }
    else
    {
        mod = upper->module;
        line = upper->line;
    }

    /* Handle the SIP version number pseudo-timeline. */
    if (line < 0)
    {
        if (lower != NULL && SIP_VERSION < lower->order)
            return FALSE;

        if (upper != NULL && SIP_VERSION >= upper->order)
            return FALSE;

        return TRUE;
    }

    for (qd = mod->qualifiers; qd != NULL; qd = qd->next)
    {
        if (qd->qtype != time_qualifier || qd->line != line)
            continue;

        if (selectedQualifier(neededQualifiers, qd))
        {
            if (lower != NULL && qd->order < lower->order)
                return FALSE;

            if (upper != NULL && qd->order >= upper->order)
                return FALSE;

            return TRUE;
        }
    }

    /*
     * If there is no upper bound then assume the expression is true unless
     * the lower bound is a backstop.
     */
    if (upper == NULL)
        return !isBackstop(lower);

    /*
     * If the upper limit corresponds to a backstop then assume the expression
     * is true.
     */
    return isBackstop(upper);
}


/*
 * See if a qualifier is a backstop.
 */
static int isBackstop(qualDef *qd)
{
    stringList *sl;

    for (sl = backstops; sl != NULL; sl = sl->next)
        if (strcmp(qd->name, sl->s) == 0)
            return TRUE;

    return FALSE;
}


/*
 * Return the value of an expression involving a single platform or feature.
 */
static int platOrFeature(char *name,int optnot)
{
    int this;
    qualDef *qd;

    if ((qd = findQualifier(name)) == NULL || qd -> qtype == time_qualifier)
        yyerror("No such platform or feature");

    /* Assume this sub-expression is false. */

    this = FALSE;

    if (qd -> qtype == feature_qualifier)
    {
        if (!excludedFeature(excludedQualifiers, qd))
            this = TRUE;
    }
    else if (selectedQualifier(neededQualifiers, qd))
    {
        this = TRUE;
    }

    if (optnot)
        this = !this;

    return this;
}


/*
 * Return TRUE if the given qualifier is excluded.
 */
int excludedFeature(stringList *xsl, qualDef *qd)
{
    while (xsl != NULL)
    {
        if (strcmp(qd->name, xsl->s) == 0)
            return TRUE;

        xsl = xsl->next;
    }

    return !qd->default_enabled;
}


/*
 * Return TRUE if the given qualifier is needed.
 */
int selectedQualifier(stringList *needed_qualifiers, qualDef *qd)
{
    stringList *sl;

    for (sl = needed_qualifiers; sl != NULL; sl = sl->next)
        if (strcmp(qd->name, sl->s) == 0)
            return qd->default_enabled;

    return FALSE;
}


/*
 * Return the current scope.  currentScope() is only valid if notSkipping()
 * returns non-zero.
 */
static classDef *currentScope(void)
{
    return (currentScopeIdx > 0 ? scopeStack[currentScopeIdx - 1] : NULL);
}


/*
 * Create a new qualifier.
 */
static void newQualifier(moduleDef *mod, int line, int order,
        int default_enabled, const char *name, qualType qt)
{
    /* Check it doesn't already exist. */
    if (findQualifier(name) != NULL)
        yyerror("Version is already defined");

    allocQualifier(mod, line, order, default_enabled, name, qt);
}


/*
 * Allocate a new qualifier.
 */
static qualDef *allocQualifier(moduleDef *mod, int line, int order,
        int default_enabled, const char *name, qualType qt)
{
    qualDef *qd;

    qd = sipMalloc(sizeof (qualDef));

    qd->name = name;
    qd->qtype = qt;
    qd->module = mod;
    qd->line = line;
    qd->order = order;
    qd->default_enabled = default_enabled;
    qd->next = mod->qualifiers;

    mod->qualifiers = qd;

    return qd;
}


/*
 * Create a new imported module.
 */
static void newImport(const char *filename)
{
    moduleDef *from, *mod;
    moduleListDef *mld;

    /* Create a new module if it has not already been defined. */
    for (mod = currentSpec->modules; mod != NULL; mod = mod->next)
        if (strcmp(mod->file, filename) == 0)
            break;

    from = currentModule;

    if (mod == NULL)
    {
        newModule(NULL, filename);
        mod = currentModule;
    }
    else if (from->encoding == no_type)
    {
        /* Import any defaults from the already parsed module. */
        from->encoding = mod->encoding;
    }

    /* Add the new import unless it has already been imported. */
    for (mld = from->imports; mld != NULL; mld = mld->next)
        if (mld->module == mod)
            return;

    mld = sipMalloc(sizeof (moduleListDef));
    mld->module = mod;
    mld->next = from->imports;

    from->imports = mld;
}


/*
 * Set up pointers to hook names.
 */
static void getHooks(optFlags *optflgs,char **pre,char **post)
{
    optFlag *of;

    if ((of = getOptFlag(optflgs,"PreHook",name_flag)) != NULL)
        *pre = of -> fvalue.sval;
    else
        *pre = NULL;

    if ((of = getOptFlag(optflgs,"PostHook",name_flag)) != NULL)
        *post = of -> fvalue.sval;
    else
        *post = NULL;
}


/*
 * Get the /Transfer/ option flag.
 */
static int getTransfer(optFlags *optflgs)
{
    return (getOptFlag(optflgs, "Transfer", bool_flag) != NULL);
}


/*
 * Get the /ReleaseGIL/ option flag.
 */
static int getReleaseGIL(optFlags *optflgs)
{
    return (getOptFlag(optflgs, "ReleaseGIL", bool_flag) != NULL);
}


/*
 * Get the /HoldGIL/ option flag.
 */
static int getHoldGIL(optFlags *optflgs)
{
    return (getOptFlag(optflgs, "HoldGIL", bool_flag) != NULL);
}


/*
 * Get the /Deprecated/ option flag.
 */
static int getDeprecated(optFlags *optflgs)
{
    return (getOptFlag(optflgs, "Deprecated", bool_flag) != NULL);
}


/*
 * Get the /AllowNone/ option flag.
 */
static int getAllowNone(optFlags *optflgs)
{
    return (getOptFlag(optflgs, "AllowNone", bool_flag) != NULL);
}


/*
 * Get the /DisallowNone/ option flag.
 */
static int getDisallowNone(optFlags *optflgs)
{
    return (getOptFlag(optflgs, "DisallowNone", bool_flag) != NULL);
}


/*
 * Get the /VirtualErrorHandler/ option flag.
 */
static const char *getVirtErrorHandler(optFlags *optflgs)
{
    optFlag *of = getOptFlag(optflgs, "VirtualErrorHandler", name_flag);

    if (of == NULL)
        return NULL;

    return of->fvalue.sval;
}


/*
 * Get the /DocType/ option flag.
 */
static const char *getDocType(optFlags *optflgs)
{
    optFlag *of = getOptFlag(optflgs, "DocType", string_flag);

    if (of == NULL)
        return NULL;

    deprecated("/DocType/ is deprecated\n");

    return of->fvalue.sval;
}


/*
 * Get the /TypeHintValue/ option flag.
 */
static const char *getTypeHintValue(optFlags *optflgs)
{
    optFlag *of = getOptFlag(optflgs, "TypeHintValue", string_flag);

    if (of != NULL)
        return of->fvalue.sval;

    if ((of = getOptFlag(optflgs, "DocValue", string_flag)) != NULL)
    {
        deprecated("/DocValue/ is deprecated\n");

        return of->fvalue.sval;
    }

    return NULL;
}


/*
 * Get the /TypeHint/, /TypeHintIn/ and /TypeHintOut/ option flags.
 */
static void getTypeHints(optFlags *optflgs, typeHintDef **in,
        typeHintDef **out)
{
    optFlag *of;
    typeHintDef *thd;

    if ((of = getOptFlag(optflgs, "TypeHint", string_flag)) != NULL)
        thd = newTypeHint(of->fvalue.sval);
    else
        thd = NULL;

    if ((of = getOptFlag(optflgs, "TypeHintIn", string_flag)) != NULL)
    {
        if (thd != NULL)
            yywarning("/TypeHintIn/ overrides /TypeHint/");

        *in = newTypeHint(of->fvalue.sval);
    }
    else
    {
        *in = thd;
    }

    if ((of = getOptFlag(optflgs, "TypeHintOut", string_flag)) != NULL)
    {
        if (thd != NULL)
            yywarning("/TypeHintOut/ overrides /TypeHint/");

        *out = newTypeHint(of->fvalue.sval);
    }
    else
    {
        *out = thd;
    }
}


/*
 * Get the /NoTypeHint/ option flag.
 */
static int getNoTypeHint(optFlags *optflgs)
{
    return (getOptFlag(optflgs, "NoTypeHint", bool_flag) != NULL);
}


/*
 * Return TRUE if the PyQt3 plugin was specified.
 */
int pluginPyQt3(sipSpec *pt)
{
    return stringFind(pt->plugins, "PyQt3");
}


/*
 * Return TRUE if the PyQt4 plugin was specified.
 */
int pluginPyQt4(sipSpec *pt)
{
    return stringFind(pt->plugins, "PyQt4");
}


/*
 * Return TRUE if the PyQt5 plugin was specified.
 */
int pluginPyQt5(sipSpec *pt)
{
    return stringFind(pt->plugins, "PyQt5");
}


/*
 * Return TRUE if a list of strings contains a given entry.
 */
static int stringFind(stringList *sl, const char *s)
{
    while (sl != NULL)
    {
        if (strcmp(sl->s, s) == 0)
            return TRUE;

        sl = sl->next;
    }

    return FALSE;
}


/*
 * Set the name of a module.
 */
static void setModuleName(sipSpec *pt, moduleDef *mod, const char *fullname)
{
    mod->fullname = cacheName(pt, fullname);

    if (inMainModule())
        setIsUsedName(mod->fullname);

    if ((mod->name = strrchr(fullname, '.')) != NULL)
        mod->name++;
    else
        mod->name = fullname;
}


/*
 * Define a new class and set its name.
 */
static void defineClass(scopedNameDef *snd, classList *supers, optFlags *of)
{
    classDef *cd, *c_scope = currentScope();
    typeHintDef *in, *out;

    getTypeHints(of, &in, &out);

    cd = newClass(currentSpec, class_iface, getAPIRange(of),
            scopeScopedName((c_scope != NULL ? c_scope->iff : NULL), snd),
            getVirtErrorHandler(of), in, out, getTypeHintValue(of));
    cd->supers = supers;

    pushScope(cd);
}


/*
 * Complete the definition of a class.
 */
static classDef *completeClass(scopedNameDef *snd, optFlags *of, int has_def)
{
    classDef *cd = currentScope();

    /* See if the class was defined or just declared. */
    if (has_def)
    {
        if (snd->next != NULL)
            yyerror("A scoped name cannot be given in a class/struct definition");

    }
    else if (cd->supers != NULL)
        yyerror("Class/struct has super-classes but no definition");
    else
        setIsOpaque(cd);

    finishClass(currentSpec, currentModule, cd, of);
    popScope();

    /*
     * Check that external classes have only been declared at the global scope.
     */
    if (isExternal(cd) && currentScope() != NULL)
        yyerror("External classes/structs can only be declared in the global scope");

    return cd;
}


/*
 * Add a variable to the list so that the list remains sorted.
 */
static void addVariable(sipSpec *pt, varDef *vd)
{
    varDef **at = &pt->vars;

    while (*at != NULL)
    {
        if (strcmp(vd->pyname->text, (*at)->pyname->text) < 0)
            break;

        at = &(*at)->next;
    }

    vd->next = *at;
    *at = vd;
}


/*
 * Update a type according to optional flags.
 */
static void applyTypeFlags(moduleDef *mod, argDef *ad, optFlags *flags)
{
    ad->doctype = getDocType(flags);
    getTypeHints(flags, &ad->typehint_in, &ad->typehint_out);

    if (getOptFlag(flags, "PyInt", bool_flag) != NULL)
    {
        if (ad->atype == string_type)
            ad->atype = byte_type;
        else if (ad->atype == sstring_type)
            ad->atype = sbyte_type;
        else if (ad->atype == ustring_type)
            ad->atype = ubyte_type;
    }

    if (ad->atype == string_type && !isArray(ad) && !isReference(ad))
    {
        optFlag *of;

        if ((of = getOptFlag(flags, "Encoding", string_flag)) == NULL)
        {
            if (mod->encoding != no_type)
                ad->atype = mod->encoding;
            else
                ad->atype = string_type;
        }
        else if ((ad->atype = convertEncoding(of->fvalue.sval)) == no_type)
            yyerror("The value of the /Encoding/ annotation must be one of \"ASCII\", \"Latin-1\", \"UTF-8\" or \"None\"");
    }
}


/*
 * Return the keyword argument support converted from a string.
 */
static KwArgs convertKwArgs(const char *kwargs)
{
    if (strcmp(kwargs, "None") == 0)
        return NoKwArgs;

    if (strcmp(kwargs, "All") == 0)
        return AllKwArgs;

    if (strcmp(kwargs, "Optional") == 0)
        return OptionalKwArgs;

    yyerror("The style of keyword argument support must be one of \"All\", \"Optional\" or \"None\"");
}


/*
 * Return the Format for a string.
 */
static Format convertFormat(const char *format)
{
    if (strcmp(format, "raw") == 0)
        return raw;

    if (strcmp(format, "deindented") == 0)
        return deindented;

    yyerror("The docstring format must be either \"raw\" or \"deindented\"");
}


/*
 * Return the argument type for a string with the given encoding or no_type if
 * the encoding was invalid.
 */
static argType convertEncoding(const char *encoding)
{
    if (strcmp(encoding, "ASCII") == 0)
        return ascii_string_type;

    if (strcmp(encoding, "Latin-1") == 0)
        return latin1_string_type;

    if (strcmp(encoding, "UTF-8") == 0)
        return utf8_string_type;

    if (strcmp(encoding, "None") == 0)
        return string_type;

    return no_type;
}


/*
 * Get the /API/ option flag.
 */
static apiVersionRangeDef *getAPIRange(optFlags *optflgs)
{
    optFlag *of;

    if ((of = getOptFlag(optflgs, "API", api_range_flag)) == NULL)
        return NULL;

    return of->fvalue.aval;
}


/*
 * Return the API range structure and version number corresponding to the
 * given API range.
 */
static apiVersionRangeDef *convertAPIRange(moduleDef *mod, nameDef *name,
        int from, int to)
{
    int index;
    apiVersionRangeDef *avd, **avdp;

    /* Handle the trivial case. */
    if (from == 0 && to == 0)
        return NULL;

    for (index = 0, avdp = &mod->api_ranges; (*avdp) != NULL; avdp = &(*avdp)->next, ++index)
    {
        avd = *avdp;

        if (avd->api_name == name && avd->from == from && avd->to == to)
            return avd;
    }

    /* The new one must be appended so that version numbers remain valid. */
    avd = sipMalloc(sizeof (apiVersionRangeDef));

    avd->api_name = name;
    avd->from = from;
    avd->to = to;
    avd->index = index;

    avd->next = NULL;
    *avdp = avd;

    return avd;
}


/*
 * Return the style of keyword argument support for a signature.
 */
static KwArgs keywordArgs(moduleDef *mod, optFlags *optflgs, signatureDef *sd,
        int need_name)
{
    KwArgs kwargs;
    optFlag *ka_anno, *no_ka_anno;

    /* Get the default. */
    kwargs = mod->kwargs;

    /*
     * Get the possible annotations allowing /KeywordArgs/ to have different
     * types of values.
     */
    ka_anno = findOptFlag(optflgs, "KeywordArgs");
    no_ka_anno = getOptFlag(optflgs, "NoKeywordArgs", bool_flag);

    if (no_ka_anno != NULL)
    {
        if (ka_anno != NULL)
            yyerror("/KeywordArgs/ and /NoKeywordArgs/ cannot both be specified");

        deprecated("/NoKeywordArgs/ is deprecated, use /KeywordArgs=\"None\" instead");

        kwargs = NoKwArgs;
    }
    else if (ka_anno != NULL)
    {
        /* A string value is the non-deprecated type. */
        if (ka_anno->ftype == string_flag)
        {
            kwargs = convertKwArgs(ka_anno->fvalue.sval);
        }
        else
        {
            deprecated("/KeywordArgs/ is deprecated, use /KeywordArgs=\"All\" instead");

            /* Get it again to check the type. */
            ka_anno = getOptFlag(optflgs, "KeywordArgs", bool_flag);
        }
    }

    /* An ellipsis cannot be used with keyword arguments. */
    if (sd->nrArgs > 0 && sd->args[sd->nrArgs - 1].atype == ellipsis_type)
        kwargs = NoKwArgs;

    if (kwargs != NoKwArgs)
    {
        int a, is_name = FALSE;

        /*
         * Mark argument names as being used and check there is at least one.
         */
        for (a = 0; a < sd->nrArgs; ++a)
        {
            argDef *ad = &sd->args[a];

            if (kwargs == OptionalKwArgs && ad->defval == NULL)
                continue;

            if (ad->name != NULL)
            {
                if (need_name || inMainModule())
                    setIsUsedName(ad->name);

                is_name = TRUE;
            }
        }

        if (!is_name)
            kwargs = NoKwArgs;
    }

    return kwargs;
}


/*
 * Extract the version of a string value optionally associated with a
 * particular feature.
 */
static char *convertFeaturedString(char *fs)
{
    while (fs != NULL)
    {
        char *next, *value;

        /* Individual values are ';' separated. */
        if ((next = strchr(fs, ';')) != NULL)
            *next++ = '\0';

        /* Features and values are ':' separated. */
        if ((value = strchr(fs, ':')) == NULL)
        {
            /* This is an unconditional value so just return it. */
            return strip(fs);
        }

        *value++ = '\0';

        if (isEnabledFeature(strip(fs)))
            return strip(value);

        fs = next;
    }

    /* No value was enabled. */
    return NULL;
}


/*
 * Return the stripped version of a string.
 */
static char *strip(char *s)
{
    while (*s == ' ')
        ++s;

    if (*s != '\0')
    {
        char *cp = &s[strlen(s) - 1];

        while (*cp == ' ')
            *cp-- = '\0';
    }

    return s;
}


/*
 * Return TRUE if the given feature is enabled.
 */
static int isEnabledFeature(const char *name)
{
    qualDef *qd;

    if ((qd = findQualifier(name)) == NULL || qd->qtype != feature_qualifier)
        yyerror("No such feature");

    return !excludedFeature(excludedQualifiers, qd);
}


/*
 * Add a property definition to a class.
 */
static void addProperty(sipSpec *pt, moduleDef *mod, classDef *cd,
        const char *name, const char *get, const char *set,
        codeBlock *docstring)
{
    propertyDef *pd;

    checkAttributes(pt, mod, cd, NULL, name, FALSE);

    pd = sipMalloc(sizeof (propertyDef));

    pd->name = cacheName(pt, name);
    pd->get = get;
    pd->set = set;
    appendCodeBlock(&pd->docstring, docstring);
    pd->next = cd->properties;

    cd->properties = pd;

    if (inMainModule())
        setIsUsedName(pd->name);
}


/*
 * Configure a module and return the (possibly new) current module.
 */
static moduleDef *configureModule(sipSpec *pt, moduleDef *module,
        const char *filename, const char *name, int version, int c_module,
        KwArgs kwargs, int use_arg_names, int call_super_init,
        int all_raise_py_exc, const char *def_error_handler,
        codeBlock *docstring)
{
    moduleDef *mod;

    /* Check the module hasn't already been defined. */
    for (mod = pt->modules; mod != NULL; mod = mod->next)
        if (mod->fullname != NULL && strcmp(mod->fullname->text, name) == 0)
            yyerror("Module is already defined");

    /*
     * If we are in a container module then create a component module and make
     * it current.
     */
    if (isContainer(module) || module->container != NULL)
    {
        mod = allocModule();

        mod->file = filename;
        mod->container = (isContainer(module) ? module : module->container);

        module = mod;
    }

    setModuleName(pt, module, name);
    module->kwargs = kwargs;
    module->virt_error_handler = def_error_handler;
    module->version = version;
    appendCodeBlock(&module->docstring, docstring);

    if (all_raise_py_exc)
        setAllRaisePyException(module);

    if (use_arg_names)
        setUseArgNames(module);

    if (call_super_init == 0)
        setCallSuperInitNo(module);
    else if (call_super_init > 0)
        setCallSuperInitYes(module);

    if (pt->genc < 0)
        pt->genc = c_module;
    else if (pt->genc != c_module)
        yyerror("Cannot mix C and C++ modules");

    return module;
}


/*
 * Add a Python naming rule to a module.
 */
static void addAutoPyName(moduleDef *mod, const char *remove_leading)
{
    autoPyNameDef *apnd, **apndp;

    for (apndp = &mod->autopyname; *apndp != NULL; apndp = &(*apndp)->next)
        ;

    apnd = sipMalloc(sizeof (autoPyNameDef));
    apnd->remove_leading = remove_leading;
    apnd->next = *apndp;

    *apndp = apnd;
}


/*
 * Check that no invalid or unknown annotations are given.
 */
static void checkAnnos(optFlags *annos, const char *valid[])
{
    if (parsingCSignature && annos->nrFlags != 0)
    {
        deprecated("Annotations should not be used in explicit C/C++ signatures");
    }
    else
    {
        int i;

        for (i = 0; i < annos->nrFlags; i++)
        {
            const char **name;

            for (name = valid; *name != NULL; ++name)
                if (strcmp(*name, annos->flags[i].fname) == 0)
                    break;

            if (*name == NULL)
                yywarning("Annotation is unknown");
        }
    }
}


/*
 * Check that no annotations were given.
 */
static void checkNoAnnos(optFlags *annos, const char *msg)
{
    if (annos->nrFlags != 0)
        deprecated(msg);
}


/*
 * Handle any /KeepReference/ annotation for a type.
 */
static void handleKeepReference(optFlags *optflgs, argDef *ad, moduleDef *mod)
{
    optFlag *of;

    if ((of = getOptFlag(optflgs, "KeepReference", opt_integer_flag)) != NULL)
    {
        setKeepReference(ad);

        if ((ad->key = of->fvalue.ival) < -1)
            yyerror("/KeepReference/ key cannot be negative");

        /* If there was no explicit key then auto-allocate one. */
        if (ad->key == -1)
            ad->key = mod->next_key--;
    }
}


/*
 * Configure the mapped type annotations that are also valid with mapped type
 * templates.
 */
static void mappedTypeAnnos(mappedTypeDef *mtd, optFlags *optflgs)
{
    if (getOptFlag(optflgs, "NoRelease", bool_flag) != NULL)
        setNoRelease(mtd);

    if (getAllowNone(optflgs))
        setHandlesNone(mtd);

    mtd->doctype = getDocType(optflgs);
    getTypeHints(optflgs, &mtd->typehint_in, &mtd->typehint_out);
    mtd->typehint_value = getTypeHintValue(optflgs);
}


/*
 * Initialise an argument with the derefences of another, plus a new one.
 */
static void add_new_deref(argDef *new, argDef *orig, int isconst)
{
    if ((new->nrderefs = orig->nrderefs + 1) >= MAX_NR_DEREFS)
        yyerror("Internal error - increase the value of MAX_NR_DEREFS");

    memcpy(&new->derefs[0], &orig->derefs[0], sizeof (new->derefs));
    new->derefs[orig->nrderefs] = isconst;
}


/*
 * Add the dereferences from one type to another.
 */
static void add_derefs(argDef *dst, argDef *src)
{
    int i;

    for (i = 0; i < src->nrderefs; ++i)
    {
        if (dst->nrderefs >= MAX_NR_DEREFS - 1)
            fatal("Internal error - increase the value of MAX_NR_DEREFS\n");

        dst->derefs[dst->nrderefs++] = src->derefs[i];
    }
}


/*
 * Check if a word is a Python keyword (or has been at any time).
 */
int isPyKeyword(const char *word)
{
    static const char *kwds[] = {
        "False", "None", "True", "and", "as", "assert", "break", "class",
        "continue", "def", "del", "elif", "else", "except", "finally", "for",
        "from", "global", "if", "import", "in", "is", "lambda", "nonlocal",
        "not", "or", "pass", "raise", "return", "try", "while", "with'"
        "yield",
        /* Historical keywords. */
        "exec", "print",
        NULL
    };

    const char **kwd;

    for (kwd = kwds; *kwd != NULL; ++kwd)
        if (strcmp(*kwd, word) == 0)
            return TRUE;

    return FALSE;
}


/*
 * Check there is nothing after an ellipsis.
 */
static void checkEllipsis(signatureDef *sd)
{
    int a;

    for (a = 0; a < sd->nrArgs; ++a)
        if (sd->args[a].atype == ellipsis_type && a < sd->nrArgs - 1)
            yyerror("An ellipsis must be at the end of the argument list if /NoArgParser/ is not specified");
}
