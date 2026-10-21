# PageTitleFiltering::testTitleXSS()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1650–1685 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1650-L1685)
- **Class:** [PageTitleFiltering](../PageTitleFiltering.md)
- **Module/theme:** system

## Signature

```php
function testTitleXSS()
```

## Documentation

```text
Test if the title of the site is XSS proof.
```

## Code

```php
  function testTitleXSS() {
    // Set some title with JavaScript and HTML chars to escape.
    $title = '</title><script type="text/javascript">alert("Title XSS!");</script> & < > " \' ';
    $title_filtered = check_plain($title);

    $slogan = '<script type="text/javascript">alert("Slogan XSS!");</script>';
    $slogan_filtered = filter_xss_admin($slogan);

    // Activate needed appearance settings.
    $edit = array(
      'toggle_name'           => TRUE,
      'toggle_slogan'         => TRUE,
      'toggle_main_menu'      => TRUE,
      'toggle_secondary_menu' => TRUE,
    );
    $this->drupalPost('admin/appearance/settings', $edit, t('Save configuration'));

    // Set title and slogan.
    $edit = array(
      'site_name'    => $title,
      'site_slogan'  => $slogan,
    );
    $this->drupalPost('admin/config/system/site-information', $edit, t('Save configuration'));

    // Load frontpage.
    $this->drupalGet('');

    // Test the title.
    $this->assertNoRaw($title, 'Check for the unfiltered version of the title.');
    // Adding </title> so we do not test the escaped version from drupal_set_title().
    $this->assertRaw($title_filtered . '</title>', 'Check for the filtered version of the title.');

    // Test the slogan.
    $this->assertNoRaw($slogan, 'Check for the unfiltered version of the slogan.');
    $this->assertRaw($slogan_filtered, 'Check for the filtered version of the slogan.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
