# SearchNumberMatchingTestCase::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1374–1407 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1374-L1407)
- **Class:** [SearchNumberMatchingTestCase](../SearchNumberMatchingTestCase.md)
- **Module/theme:** search

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('search');

    $this->test_user = $this->drupalCreateUser(array('search content', 'access content', 'administer nodes', 'access site reports'));
    $this->drupalLogin($this->test_user);

    // Define a group of numbers that should all match each other --
    // numbers with internal punctuation should match each other, as well
    // as numbers with and without leading zeros and leading/trailing
    // . and -.
    $this->numbers = array(
      '123456789',
      '12/34/56789',
      '12.3456789',
      '12-34-56789',
      '123,456,789',
      '-123456789',
      '0123456789',
    );

    foreach ($this->numbers as $num) {
      $info = array(
        'body' => array(LANGUAGE_NONE => array(array('value' => $num))),
        'type' => 'page',
        'language' => LANGUAGE_NONE,
      );
      $this->nodes[] = $this->drupalCreateNode($info);
    }

    // Run cron to ensure the content is indexed.
    $this->cronRun();
    $this->drupalGet('admin/reports/dblog');
    $this->assertText(t('Cron run completed'), 'Log shows cron run completed');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
