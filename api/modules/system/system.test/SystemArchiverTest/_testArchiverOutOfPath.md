# SystemArchiverTest::_testArchiverOutOfPath()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3274–3297 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3274-L3297)
- **Class:** [SystemArchiverTest](../SystemArchiverTest.md)
- **Module/theme:** system

## Signature

```php
public function _testArchiverOutOfPath($archive, $message)
```

## Documentation

```text
Helper to test out-of-path extraction protection.
```

## Code

```php
  public function _testArchiverOutOfPath($archive, $message) {
    $src_tarball = DRUPAL_ROOT . '/modules/system/tests/' . $archive;
    $tarball = file_directory_temp() . '/' . $archive;
    file_unmanaged_copy($src_tarball, $tarball);
    try {
      $archiver = archiver_get_archiver($tarball);
    } catch (Exception $e) {
      // The file's not there (this is not part of the test).
      $this->assertTrue(FALSE, $e);
      return;
    }

    $extract_dir = file_directory_temp() . '/testArchiverTarball';
    $caught_exception = FALSE;
    try {
      // Drupal's \ArchiverTar::extract() doesn't support symlinks, so we have
      // to access the underlying Archive_Tar object.
      $archiver->getArchive()->extract($extract_dir, FALSE, TRUE);
    }
    catch (Exception $e) {
      $caught_exception = (strpos($e->getMessage(), 'Out-of-path file extraction') !== FALSE);
    }
    $this->assertTrue($caught_exception, $message);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
