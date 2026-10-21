# DrupalTestCase

- **Type:** Class
- **File:** [`modules/simpletest/drupal_web_test_case.php`](_file.md), lines 20–746 · [local source](../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L20-L746)
- **Module/theme:** simpletest

## Signature

```php
abstract class DrupalTestCase
```

## Documentation

```text
Base class for Drupal tests.

Do not extend this class, use one of the subclasses in this file.
```

## Properties

### $testId

```php
protected $testId;
```

```text
The test run ID.

@var string
```

### $databasePrefix

```php
protected $databasePrefix = NULL;
```

```text
The database prefix of this test run.

@var string
```

### $originalFileDirectory

```php
protected $originalFileDirectory = NULL;
```

```text
The original file directory, before it was changed for testing purposes.

@var string
```

### $verboseDirectoryUrl

```php
protected $verboseDirectoryUrl;
```

```text
URL to the verbose output file directory.

@var string
```

### $timeLimit

```php
protected $timeLimit = 500;
```

```text
Time limit for the test.
```

### $useSetupInstallationCache

```php
public $useSetupInstallationCache = FALSE;
```

```text
Whether to cache the installation part of the setUp() method.

@var bool
```

### $useSetupModulesCache

```php
public $useSetupModulesCache = FALSE;
```

```text
Whether to cache the modules installation part of the setUp() method.

@var bool
```

### $originalLanguage

```php
protected $originalLanguage;
```

```text
The original language.
```

### $originalLanguageDefault

```php
protected $originalLanguageDefault;
```

```text
The original default language.
```

### $originalTheme

```php
protected $originalTheme;
```

```text
The original theme.
```

### $originalThemeKey

```php
protected $originalThemeKey;
```

```text
The original theme key.
```

### $originalThemePath

```php
protected $originalThemePath;
```

```text
The original theme path.
```

### $results

```php
public $results = array(
    '#pass' => 0,
    '#fail' => 0,
    '#exception' => 0,
    '#debug' => 0,
  );
```

```text
Current results of this test case.

@var Array
```

### $assertions

```php
protected $assertions = array();
```

```text
Assertions thrown in that test case.

@var Array
```

### $skipClasses

```php
protected $skipClasses = array(__CLASS__ => TRUE);
```

```text
This class is skipped when looking for the source of an assertion.

When displaying which function an assert comes from, it's not too useful
to see "drupalWebTestCase->drupalLogin()', we would like to see the test
that called it. So we need to skip the classes defining these helper
methods.
```

### $setup

```php
protected $setup = FALSE;
```

```text
Flag to indicate whether the test has been set up.

The setUp() method isolates the test from the parent Drupal site by
creating a random prefix for the database and setting up a clean file
storage directory. The tearDown() method then cleans up this test
environment. We must ensure that setUp() has been run. Otherwise,
tearDown() will act on the parent Drupal site rather than the test
environment, destroying live data.
```

### $setupDatabasePrefix

```php
protected $setupDatabasePrefix = FALSE;
```

### $setupEnvironment

```php
protected $setupEnvironment = FALSE;
```

## Methods (derived index)

- [__construct()](DrupalTestCase/__construct.md) — Constructor for DrupalTestCase.
- [assert()](DrupalTestCase/assert.md) — Internal helper: stores the assert.
- [getDatabaseConnection()](DrupalTestCase/getDatabaseConnection.md) — Returns the database connection to the site running Simpletest.
- [insertAssert()](DrupalTestCase/insertAssert.md) — Store an assertion from outside the testing context.
- [deleteAssert()](DrupalTestCase/deleteAssert.md) — Delete an assertion record by message ID.
- [getAssertionCall()](DrupalTestCase/getAssertionCall.md) — Cycles through backtrace until the first non-assertion method is found.
- [assertTrue()](DrupalTestCase/assertTrue.md) — Check to see if a value is not false (not an empty string, 0, NULL, or FALSE).
- [assertFalse()](DrupalTestCase/assertFalse.md) — Check to see if a value is false (an empty string, 0, NULL, or FALSE).
- [assertNull()](DrupalTestCase/assertNull.md) — Check to see if a value is NULL.
- [assertNotNull()](DrupalTestCase/assertNotNull.md) — Check to see if a value is not NULL.
- [assertEqual()](DrupalTestCase/assertEqual.md) — Check to see if two values are equal.
- [assertNotEqual()](DrupalTestCase/assertNotEqual.md) — Check to see if two values are not equal.
- [assertIdentical()](DrupalTestCase/assertIdentical.md) — Check to see if two values are identical.
- [assertNotIdentical()](DrupalTestCase/assertNotIdentical.md) — Check to see if two values are not identical.
- [pass()](DrupalTestCase/pass.md) — Fire an assertion that is always positive.
- [fail()](DrupalTestCase/fail.md) — Fire an assertion that is always negative.
- [error()](DrupalTestCase/error.md) — Fire an error assertion.
- [verbose()](DrupalTestCase/verbose.md) — Logs a verbose message in a text file.
- [run()](DrupalTestCase/run.md) — Run all tests in this class.
- [errorHandler()](DrupalTestCase/errorHandler.md) — Handle errors during test runs.
- [exceptionHandler()](DrupalTestCase/exceptionHandler.md) — Handle exceptions.
- [randomString()](DrupalTestCase/randomString.md) — Generates a random string of ASCII characters of codes 32 to 126.
- [randomName()](DrupalTestCase/randomName.md) — Generates a random string containing letters and numbers.
- [generatePermutations()](DrupalTestCase/generatePermutations.md) — Converts a list of possible parameters into a stack of permutations.

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
