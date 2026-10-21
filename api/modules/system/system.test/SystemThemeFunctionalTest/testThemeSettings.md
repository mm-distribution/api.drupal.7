# SystemThemeFunctionalTest::testThemeSettings()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1921–2016 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1921-L2016)
- **Class:** [SystemThemeFunctionalTest](../SystemThemeFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testThemeSettings()
```

## Documentation

```text
Test the theme settings form.
```

## Code

```php
  function testThemeSettings() {
    // Specify a filesystem path to be used for the logo.
    $file = current($this->drupalGetTestFiles('image'));
    $file_relative = strtr($file->uri, array('public:/' => variable_get('file_public_path', conf_path() . '/files')));
    $default_theme_path = 'themes/stark';

    $supported_paths = array(
      // Raw stream wrapper URI.
      $file->uri => array(
        'form' => file_uri_target($file->uri),
        'src' => file_create_url($file->uri),
      ),
      // Relative path within the public filesystem.
      file_uri_target($file->uri) => array(
        'form' => file_uri_target($file->uri),
        'src' => file_create_url($file->uri),
      ),
      // Relative path to a public file.
      $file_relative => array(
        'form' => $file_relative,
        'src' => file_create_url($file->uri),
      ),
      // Relative path to an arbitrary file.
      'misc/druplicon.png' => array(
        'form' => 'misc/druplicon.png',
        'src' => $GLOBALS['base_url'] . '/' . 'misc/druplicon.png',
      ),
      // Relative path to a file in a theme.
      $default_theme_path . '/logo.png' => array(
        'form' => $default_theme_path . '/logo.png',
        'src' => $GLOBALS['base_url'] . '/' . $default_theme_path . '/logo.png',
      ),
    );
    foreach ($supported_paths as $input => $expected) {
      $edit = array(
        'default_logo' => FALSE,
        'logo_path' => $input,
      );
      $this->drupalPost('admin/appearance/settings', $edit, t('Save configuration'));
      $this->assertNoText('The custom logo path is invalid.');
      $this->assertFieldByName('logo_path', $expected['form']);

      // Verify the actual 'src' attribute of the logo being output.
      $this->drupalGet('');
      $elements = $this->xpath('//*[@id=:id]/img', array(':id' => 'logo'));
      $this->assertEqual((string) $elements[0]['src'], $expected['src']);
    }

    $unsupported_paths = array(
      // Stream wrapper URI to non-existing file.
      'public://whatever.png',
      'private://whatever.png',
      'temporary://whatever.png',
      // Bogus stream wrapper URIs.
      'public:/whatever.png',
      '://whatever.png',
      ':whatever.png',
      'public://',
      // Relative path within the public filesystem to non-existing file.
      'whatever.png',
      // Relative path to non-existing file in public filesystem.
      variable_get('file_public_path', conf_path() . '/files') . '/whatever.png',
      // Semi-absolute path to non-existing file in public filesystem.
      '/' . variable_get('file_public_path', conf_path() . '/files') . '/whatever.png',
      // Relative path to arbitrary non-existing file.
      'misc/whatever.png',
      // Semi-absolute path to arbitrary non-existing file.
      '/misc/whatever.png',
      // Absolute paths to any local file (even if it exists).
      drupal_realpath($file->uri),
    );
    $this->drupalGet('admin/appearance/settings');
    foreach ($unsupported_paths as $path) {
      $edit = array(
        'default_logo' => FALSE,
        'logo_path' => $path,
      );
      $this->drupalPost(NULL, $edit, t('Save configuration'));
      $this->assertText('The custom logo path is invalid.');
    }

    // Upload a file to use for the logo.
    $edit = array(
      'default_logo' => FALSE,
      'logo_path' => '',
      'files[logo_upload]' => drupal_realpath($file->uri),
    );
    $this->drupalPost('admin/appearance/settings', $edit, t('Save configuration'));

    $fields = $this->xpath($this->constructFieldXpath('name', 'logo_path'));
    $uploaded_filename = 'public://' . $fields[0]['value'];

    $this->drupalGet('');
    $elements = $this->xpath('//*[@id=:id]/img', array(':id' => 'logo'));
    $this->assertEqual($elements[0]['src'], file_create_url($uploaded_filename));
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
