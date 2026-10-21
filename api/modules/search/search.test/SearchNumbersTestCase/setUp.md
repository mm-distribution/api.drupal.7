# SearchNumbersTestCase::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1286–1326 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1286-L1326)
- **Class:** [SearchNumbersTestCase](../SearchNumbersTestCase.md)
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

    // Create content with various numbers in it.
    // Note: 50 characters is the current limit of the search index's word
    // field.
    $this->numbers = array(
      'ISBN' => '978-0446365383',
      'UPC' => '036000 291452',
      'EAN bar code' => '5901234123457',
      'negative' => '-123456.7890',
      'quoted negative' => '"-123456.7890"',
      'leading zero' => '0777777777',
      'tiny' => '111',
      'small' => '22222222222222',
      'medium' => '333333333333333333333333333',
      'large' => '444444444444444444444444444444444444444',
      'gigantic' => '5555555555555555555555555555555555555555555555555',
      'over fifty characters' => '666666666666666666666666666666666666666666666666666666666666',
      'date', '01/02/2009',
      'commas', '987,654,321',
    );

    foreach ($this->numbers as $doc => $num) {
      $info = array(
        'body' => array(LANGUAGE_NONE => array(array('value' => $num))),
        'type' => 'page',
        'language' => LANGUAGE_NONE,
        'title' => $doc . ' number',
      );
      $this->nodes[$doc] = $this->drupalCreateNode($info);
    }

    // Run cron to ensure the content is indexed.
    $this->cronRun();
    $this->drupalGet('admin/reports/dblog');
    $this->assertText(t('Cron run completed'), 'Log shows cron run completed');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
