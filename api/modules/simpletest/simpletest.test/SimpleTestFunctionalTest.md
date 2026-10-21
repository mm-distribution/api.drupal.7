# SimpleTestFunctionalTest

- **Type:** Class
- **File:** [`modules/simpletest/simpletest.test`](_file.md), lines 8–344 · [local source](../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L8-L344)
- **Module/theme:** simpletest

## Signature

```php
class SimpleTestFunctionalTest extends DrupalWebTestCase
```

## Documentation

_No docblock in source._

## Properties

### $childTestResults

```php
protected $childTestResults;
```

```text
The results array that has been parsed by getTestResults().
```

### $test_ids

```php
protected $test_ids = array();
```

```text
Store the test ID from each test run for comparison, to ensure they are
incrementing.
```

### $pass

```php
protected $pass;
```

```text
The pass message.
```

### $fail

```php
protected $fail;
```

```text
The fail message.
```

### $valid_permission

```php
protected $valid_permission;
```

```text
The valid permission.
```

### $invalid_permission

```php
protected $invalid_permission;
```

```text
The invalid permission.
```

## Methods (derived index)

- [getInfo()](SimpleTestFunctionalTest/getInfo.md)
- [setUp()](SimpleTestFunctionalTest/setUp.md)
- [testInternalBrowser()](SimpleTestFunctionalTest/testInternalBrowser.md) — Test the internal browsers functionality.
- [testUserAgentValidation()](SimpleTestFunctionalTest/testUserAgentValidation.md) — Test validation of the User-Agent header we use to perform test requests.
- [testWebTestRunner()](SimpleTestFunctionalTest/testWebTestRunner.md) — Make sure that tests selected through the web interface are run and that the results are displayed correctly.
- [stubTest()](SimpleTestFunctionalTest/stubTest.md) — Test to be run and the results confirmed.
- [assertNothing()](SimpleTestFunctionalTest/assertNothing.md) — Assert nothing.
- [confirmStubTestResults()](SimpleTestFunctionalTest/confirmStubTestResults.md) — Confirm that the stub test produced the desired results.
- [getTestIdFromResults()](SimpleTestFunctionalTest/getTestIdFromResults.md) — Fetch the test id from the test results.
- [assertAssertion()](SimpleTestFunctionalTest/assertAssertion.md) — Assert that an assertion with the specified values is displayed in the test results.
- [getTestResults()](SimpleTestFunctionalTest/getTestResults.md) — Get the results from a test and store them in the class array $results.
- [getResultFieldSet()](SimpleTestFunctionalTest/getResultFieldSet.md) — Get the fieldset containing the results for group this test is in.
- [asText()](SimpleTestFunctionalTest/asText.md) — Extract the text contained by the element.
- [inCURL()](SimpleTestFunctionalTest/inCURL.md) — Check if the test is being run from inside a CURL request.

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
