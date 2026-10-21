# SimpleTestFunctionalTest::stubTest()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 177–199 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L177-L199)
- **Class:** [SimpleTestFunctionalTest](../SimpleTestFunctionalTest.md)
- **Module/theme:** simpletest

## Signature

```php
function stubTest()
```

## Documentation

```text
Test to be run and the results confirmed.
```

## Code

```php
  function stubTest() {
    $this->pass($this->pass);
    $this->fail($this->fail);

    $this->drupalCreateUser(array($this->valid_permission));
    $this->drupalCreateUser(array($this->invalid_permission));

    $this->pass(t('Test ID is @id.', array('@id' => $this->testId)));

    // Generates a warning.
    $a = '';
    foreach ($a as $b) {

    }

    // Call an assert function specific to that class.
    $this->assertNothing();

    // Generates 3 warnings inside a PHP function.
    simplexml_load_string('<fake>');

    debug('Foo', 'Debug');
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
