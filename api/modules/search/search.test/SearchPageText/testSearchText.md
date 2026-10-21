# SearchPageText::testSearchText()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 270–310 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L270-L310)
- **Class:** [SearchPageText](../SearchPageText.md)
- **Module/theme:** search

## Signature

```php
function testSearchText()
```

## Documentation

```text
Tests the failed search text, and various other text on the search page.
```

## Code

```php
  function testSearchText() {
    $this->drupalLogin($this->searching_user);
    $this->drupalGet('search/node');
    $this->assertText(t('Enter your keywords'));
    $this->assertText(t('Search'));
    $title = t('Search') . ' | Drupal';
    $this->assertTitle($title, 'Search page title is correct');

    $edit = array();
    $edit['keys'] = 'bike shed ' . $this->randomName();
    $this->drupalPost('search/node', $edit, t('Search'));
    $this->assertText(t('Consider loosening your query with OR. bike OR shed will often show more results than bike shed.'), 'Help text is displayed when search returns no results.');
    $this->assertText(t('Search'));
    $this->assertTitle($title, 'Search page title is correct');

    $edit['keys'] = $this->searching_user->name;
    $this->drupalPost('search/user', $edit, t('Search'));
    $this->assertText(t('Search'));
    $this->assertTitle($title, 'Search page title is correct');

    // Test that search keywords containing slashes are correctly loaded
    // from the path and displayed in the search form.
    $arg = $this->randomName() . '/' . $this->randomName();
    $this->drupalGet('search/node/' . $arg);
    $input = $this->xpath("//input[@id='edit-keys' and @value='{$arg}']");
    $this->assertFalse(empty($input), 'Search keys with a / are correctly set as the default value in the search box.');

    // Test a search input exceeding the limit of AND/OR combinations to test
    // the Denial-of-Service protection.
    $limit = variable_get('search_and_or_limit', 7);
    $keys = array();
    for ($i = 0; $i < $limit + 1; $i++) {
      $keys[] = $this->randomName(3);
      if ($i % 2 == 0) {
        $keys[] = 'OR';
      }
    }
    $edit['keys'] = implode(' ', $keys);
    $this->drupalPost('search/node', $edit, t('Search'));
    $this->assertRaw(t('Your search used too many AND/OR expressions. Only the first @count terms were included in this search.', array('@count' => $limit)));
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
