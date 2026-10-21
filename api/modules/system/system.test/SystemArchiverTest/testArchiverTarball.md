# SystemArchiverTest::testArchiverTarball()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3225–3261 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3225-L3261)
- **Class:** [SystemArchiverTest](../SystemArchiverTest.md)
- **Module/theme:** system

## Signature

```php
public function testArchiverTarball()
```

## Documentation

```text
Tests interacting with a tarball archive.
```

## Code

```php
  public function testArchiverTarball() {
    $src_tarball = DRUPAL_ROOT . '/' . drupal_get_path('module', 'system') . '/tests/system_test_archive.tar.gz';
    $tmp = file_directory_temp();
    $tarball = $tmp . '/' . basename($src_tarball);
    file_unmanaged_copy($src_tarball, $tarball);
    try {
      $archiver = archiver_get_archiver($tarball);
    }
    catch (Exception $e) {
      // The file's not there (this is not part of the test).
      $this->assertTrue(FALSE, $e);
      return;
    }

    // Test \ArchiverTar::listContents
    $listing = $archiver->listContents();
    $this->assertEqual(count($listing), 4, 'Tarball listing has 4 entries.');
    $this->assertTrue((strpos(implode(',', $listing), 'tarball.module') !== FALSE), 'Tarball listing includes tarball.module');

    // Test \ArchiverTar::extract
    $extract_dir = file_directory_temp() . '/testArchiverTarball';
    $archiver->extract($extract_dir);
    $this->assertTrue(file_exists($extract_dir . '/system_test_archive/test.txt'), 'test.txt extracted from tarball');
    $this->assertEqual(count(glob($extract_dir . '/system_test_archive/*')), 3, '3 files extracted from tarball');

    // Test \ArchiverTar::add
    $extra_file = DRUPAL_ROOT . '/misc/druplicon.png';
    $archiver->add($extra_file);
    $new_listing = $archiver->listContents();
    // \ArchiverTar::add probably should not add the new file with its absolute
    // path. However that's how \Archive_Tar::add works. If we wanted to modify
    // the file path within the archive, we could call \Archive_Tar::addModify
    // directly and use its additional parameters. That could be done using
    // \ArchiverTar::getArchive like in _testArchiverOutOfPath() which calls
    // \Archive_Tar::extract directly.
    $this->assertTrue(in_array($extra_file, $new_listing), 'Druplicon added to tarball');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
