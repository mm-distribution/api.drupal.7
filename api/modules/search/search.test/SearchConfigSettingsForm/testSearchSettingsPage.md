# SearchConfigSettingsForm::testSearchSettingsPage()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1485–1522 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1485-L1522)
- **Class:** [SearchConfigSettingsForm](../SearchConfigSettingsForm.md)
- **Module/theme:** search

## Signature

```php
function testSearchSettingsPage()
```

## Documentation

```text
Verify the search settings form.
```

## Code

```php
  function testSearchSettingsPage() {

    // Test that the settings form displays the correct count of items left to index.
    $this->drupalGet('admin/config/search/settings');
    $this->assertText(t('There are @count items left to index.', array('@count' => 0)));

    // Test the re-index button.
    $this->drupalPost('admin/config/search/settings', array(), t('Re-index site'));
    $this->assertText(t('Are you sure you want to re-index the site'));
    $this->drupalPost('admin/config/search/settings/reindex', array(), t('Re-index site'));
    $this->assertText(t('The index will be rebuilt'));
    $this->drupalGet('admin/config/search/settings');
    $this->assertText(t('There is 1 item left to index.'));

    // Test that the form saves with the default values.
    $this->drupalPost('admin/config/search/settings', array(), t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'Form saves with the default values.');

    // Test that the form does not save with an invalid word length.
    $edit = array(
      'minimum_word_size' => $this->randomName(3),
    );
    $this->drupalPost('admin/config/search/settings', $edit, t('Save configuration'));
    $this->assertNoText(t('The configuration options have been saved.'), 'Form does not save with an invalid word length.');

    // Test logging setting. It should be on by default.
    $text = $this->randomName(5);
    $this->drupalPost('search/node', array('keys' => $text), t('Search'));
    $this->drupalGet('admin/reports/dblog');
    $this->assertLink('Searched Content for ' . $text . '.', 0, 'Search was logged');

    // Turn off logging.
    variable_set('search_logging', FALSE);
    $text = $this->randomName(5);
    $this->drupalPost('search/node', array('keys' => $text), t('Search'));
    $this->drupalGet('admin/reports/dblog');
    $this->assertNoLink('Searched Content for ' . $text . '.', 'Search was not logged');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
