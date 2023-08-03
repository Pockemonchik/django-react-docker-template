import React, { useEffect } from "react";
import { Layout, Menu, message, Button, Col, Row } from "antd";
import { AuthPage } from "../pages/AuthPage/AuthPage";
import { observer } from "mobx-react-lite";
import { useRootStore } from "../store";
import { useState } from "react";
import { useLocation } from "react-router-dom";
import "./App.css";

export const App = observer(() => {
  const { currentUserStore } =
    useRootStore();
  const location = useLocation();
  const [collapsed, setCollapsed] = useState(true);
  const [selectedModule, setSelectedModule] = useState(1);
  useEffect(() => {
  
  }, []);

  return currentUserStore.isAuth ? (
    <Layout hasSider style={{ minHeight: "100vh" }}>
      <Layout.Sider
        collapsible
        trigger={null}
        collapsed={collapsed}
        onCollapse={(value) => setCollapsed(value)}
        style={{
          backgroundColor: "rgba(0, 120, 255, 0.02)",
        }}
      >
        <p>Шаблон</p>
      </Layout.Sider>
    </Layout>
  ) : (
    <AuthPage />
  );
});
