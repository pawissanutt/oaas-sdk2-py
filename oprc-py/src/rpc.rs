use oprc_invoke::proxy::ObjectProxy;
use pyo3::{exceptions::PyRuntimeError, Py, PyResult, Python};

use crate::model::{InvocationRequest, InvocationResponse, ObjectInvocationRequest};

/// Manages RPC invocations using an ObjectProxy.
#[pyo3_stub_gen::derive::gen_stub_pyclass]
#[pyo3::pyclass]
pub struct RpcManager {
    proxy: ObjectProxy,
}

impl RpcManager {
    /// Creates a new RpcManager with a Zenoh session.
    pub fn new(z_session: zenoh::Session) -> Self {
        RpcManager {
            proxy: ObjectProxy::new(z_session),
        }
    }
}

#[pyo3_stub_gen::derive::gen_stub_pymethods]
#[pyo3::pymethods]
impl RpcManager {
    /// Invokes a function based on the provided InvocationRequest.
    pub async fn invoke_fn(&self, req: Py<InvocationRequest>) -> PyResult<InvocationResponse> {
        let proto_req = Python::with_gil(|py| {
            let req = req.into_bound(py);
            let req = req.borrow();
            req.into_proto()
        });
        let result = self.proxy.invoke_fn_with_req(&proto_req).await;
        result
            .map_err(|e| PyRuntimeError::new_err(e.to_string()))
            .map(|resp| InvocationResponse::from(resp))
    }

    /// Invokes an object method based on the provided ObjectInvocationRequest.
    pub async fn invoke_obj(
        &self,
        req: Py<ObjectInvocationRequest>,
    ) -> PyResult<InvocationResponse> {
        let proto_req = Python::with_gil(|py| {
            let req = req.into_bound(py);
            let req = req.borrow();
            req.into_proto()
        });
        let result = self.proxy.invoke_obj_with_req(&proto_req).await;
        result
            .map_err(|e| PyRuntimeError::new_err(e.to_string()))
            .map(|resp| InvocationResponse::from(resp))
    }
}
