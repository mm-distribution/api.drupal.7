# FrontPageTestCase::testDrupalIsFrontPage()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1718–1742 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1718-L1742)
- **Class:** [FrontPageTestCase](../FrontPageTestCase.md)
- **Module/theme:** system

## Signature

```php
function testDrupalIsFrontPage()
```

## Documentation

```text
Test front page functionality.
```

## Code

```php
  function testDrupalIsFrontPage() {
    $this->drupalGet('');
    $this->assertText(t('On front page.'), 'Path is the front page.');
    $this->drupalGet('node');
    $this->assertText(t('On front page.'), 'Path is the front page.');
    $this->drupalGet($this->node_path);
    $this->assertNoText(t('On front page.'), 'Path is not the front page.');

    // Change the front page to an invalid path.
    $edit = array('site_frontpage' => 'kittens');
    $this->drupalPost('admin/config/system/site-information', $edit, t('Save configuration'));
    $this->assertText(t("The path '@path' is either invalid or you do not have access to it.", array('@path' => $edit['site_frontpage'])));

    // Change the front page to a valid path.
    $edit['site_frontpage'] = $this->node_path;
    $this->drupalPost('admin/config/system/site-information', $edit, t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'The front page path has been saved.');

    $this->drupalGet('');
    $this->assertText(t('On front page.'), 'Path is the front page.');
    $this->drupalGet('node');
    $this->assertNoText(t('On front page.'), 'Path is not the front page.');
    $this->drupalGet($this->node_path);
    $this->assertText(t('On front page.'), 'Path is the front page.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
