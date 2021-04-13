import pytest

from decisionengine.framework.dataspace import dataspace
from decisionengine.framework.dataspace.datasource import DataSource

def test_datablock_config_finds_bad():
    with pytest.raises(dataspace.DataSpaceConfigurationError) as e:
        dataspace.DataSpace({})
    assert e.match('missing dataspace information')

    with pytest.raises(dataspace.DataSpaceConfigurationError) as e:
        dataspace.DataSpace({'dataspace': 'asdf'})
    assert e.match('dataspace key must correspond to a dictionary')

    with pytest.raises(dataspace.DataSpaceConfigurationError) as e:
        dataspace.DataSpace({'dataspace': {'asdf': 'asdf'}})
    assert e.match('Invalid dataspace configuration')

def test_has_methods_we_expect():
    getattr(DataSource, 'taskmanager_table')
    getattr(DataSource, 'dataproduct_table')
    getattr(DataSource, 'header_table')
    getattr(DataSource, 'metadata_table')

    assert True is callable(DataSource)
    assert True is callable(DataSource.get_schema)
    assert True is callable(DataSource.connect)
    assert True is callable(DataSource.create_tables)
    assert True is callable(DataSource.insert)
    assert True is callable(DataSource.update)
    assert True is callable(DataSource.get_dataproduct)
    assert True is callable(DataSource.get_dataproducts)
    assert True is callable(DataSource.get_header)
    assert True is callable(DataSource.get_metadata)
    assert True is callable(DataSource.get_datablock)
    assert True is callable(DataSource.duplicate_datablock)
    assert True is callable(DataSource.get_last_generation_id)
    assert True is callable(DataSource.close)
    assert True is callable(DataSource.store_taskmanager)
    assert True is callable(DataSource.get_taskmanagers)
    assert True is callable(DataSource.get_taskmanager)
    assert True is callable(DataSource.delete_data_older_than)
