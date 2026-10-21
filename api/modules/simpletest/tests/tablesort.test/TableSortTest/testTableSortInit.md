# TableSortTest::testTableSortInit()

- **Type:** Method
- **File:** [`modules/simpletest/tests/tablesort.test`](../_file.md), lines 45–165 · [local source](../../../../../../source/modules/simpletest/tests/tablesort.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/tablesort.test#L45-L165)
- **Class:** [TableSortTest](../TableSortTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testTableSortInit()
```

## Documentation

```text
Test tablesort_init().
```

## Code

```php
  function testTableSortInit() {

    // Test simple table headers.

    $headers = array('foo', 'bar', 'baz');
    // Reset $_GET to prevent parameters from Simpletest and Batch API ending
    // up in $ts['query'].
    $_GET = array('q' => 'jahwohl');
    $expected_ts = array(
      'name' => 'foo',
      'sql' => '',
      'sort' => 'asc',
      'query' => array(),
    );
    $ts = tablesort_init($headers);
    $this->verbose(strtr('$ts: <pre>!ts</pre>', array('!ts' => check_plain(var_export($ts, TRUE)))));
    $this->assertEqual($ts, $expected_ts, 'Simple table headers sorted correctly.');

    // Test with simple table headers plus $_GET parameters that should _not_
    // override the default.

    $_GET = array(
      'q' => 'jahwohl',
      // This should not override the table order because only complex
      // headers are overridable.
      'order' => 'bar',
    );
    $ts = tablesort_init($headers);
    $this->verbose(strtr('$ts: <pre>!ts</pre>', array('!ts' => check_plain(var_export($ts, TRUE)))));
    $this->assertEqual($ts, $expected_ts, 'Simple table headers plus non-overriding $_GET parameters sorted correctly.');

    // Test with simple table headers plus $_GET parameters that _should_
    // override the default.

    $_GET = array(
      'q' => 'jahwohl',
      'sort' => 'DESC',
      // Add an unrelated parameter to ensure that tablesort will include
      // it in the links that it creates.
      'alpha' => 'beta',
    );
    $expected_ts['sort'] = 'desc';
    $expected_ts['query'] = array('alpha' => 'beta');
    $ts = tablesort_init($headers);
    $this->verbose(strtr('$ts: <pre>!ts</pre>', array('!ts' => check_plain(var_export($ts, TRUE)))));
    $this->assertEqual($ts, $expected_ts, 'Simple table headers plus $_GET parameters sorted correctly.');

    // Test complex table headers.

    $headers = array(
      'foo',
      array(
        'data' => '1',
        'field' => 'one',
        'sort' => 'asc',
        'colspan' => 1,
      ),
      array(
        'data' => '2',
        'field' => 'two',
        'sort' => 'desc',
      ),
    );
    // Reset $_GET from previous assertion.
    $_GET = array(
      'q' => 'jahwohl',
      'order' => '2',
    );
    $ts = tablesort_init($headers);
    $expected_ts = array(
      'name' => '2',
      'sql' => 'two',
      'sort' => 'desc',
      'query' => array(),
    );
    $this->verbose(strtr('$ts: <pre>!ts</pre>', array('!ts' => check_plain(var_export($ts, TRUE)))));
    $this->assertEqual($ts, $expected_ts, 'Complex table headers sorted correctly.');

    // Test complex table headers plus $_GET parameters that should _not_
    // override the default.

    $_GET = array(
      'q' => 'jahwohl',
      // This should not override the table order because this header does not
      // exist.
      'order' => 'bar',
    );
    $ts = tablesort_init($headers);
    $expected_ts = array(
      'name' => '1',
      'sql' => 'one',
      'sort' => 'asc',
      'query' => array(),
    );
    $this->verbose(strtr('$ts: <pre>!ts</pre>', array('!ts' => check_plain(var_export($ts, TRUE)))));
    $this->assertEqual($ts, $expected_ts, 'Complex table headers plus non-overriding $_GET parameters sorted correctly.');
    unset($_GET['sort'], $_GET['order'], $_GET['alpha']);

    // Test complex table headers plus $_GET parameters that _should_
    // override the default.

    $_GET = array(
      'q' => 'jahwohl',
      'order' => '1',
      'sort' => 'ASC',
      // Add an unrelated parameter to ensure that tablesort will include
      // it in the links that it creates.
      'alpha' => 'beta',
    );
    $expected_ts = array(
      'name' => '1',
      'sql' => 'one',
      'sort' => 'asc',
      'query' => array('alpha' => 'beta'),
    );
    $ts = tablesort_init($headers);
    $this->verbose(strtr('$ts: <pre>!ts</pre>', array('!ts' => check_plain(var_export($ts, TRUE)))));
    $this->assertEqual($ts, $expected_ts, 'Complex table headers plus $_GET parameters sorted correctly.');
    unset($_GET['sort'], $_GET['order'], $_GET['alpha']);

  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/tablesort.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/tablesort.test) · Licensed GPL-2.0-or-later (see LICENSE)._
