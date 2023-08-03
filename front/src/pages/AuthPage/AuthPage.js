import React from "react";
import { Button, Form, Input,Divider } from "antd";
import "./auth.css";
import LockOutlined from "@ant-design/icons/lib/icons/LockOutlined";
import UserOutlined from "@ant-design/icons/lib/icons/UserOutlined";
import { useRootStore } from "../../store";
import { observer } from "mobx-react-lite";


export const AuthPage = observer((props) => {
    const { currentUserStore } = useRootStore()
    return (
        <div className="bg">
        <div className="authBox">
            <div className="card">
            <Divider>Вход</Divider>
                <div className="form">
                    <Form name="login"
                        onFinish={(value) => currentUserStore.login(value)}
                    >
                        <Form.Item
                            name='user'
                            rules={[
                                {
                                    required: true,
                                    message: "Пожалуйста введите логин!"
                                },
                            ]}
                        >
                            <Input
                                size="large"
                                prefix={<UserOutlined />}
                                type="text"
                                placeholder="Логин"
                                autoComplete='off'
                            />
                        </Form.Item>

                        <Form.Item
                            name="password"
                            rules={[
                                {
                                    required: true,
                                    message: "Пожалуйста введите пароль!"
                                },
                            ]}
                        >
                            <Input
                                size="large"
                                prefix={<LockOutlined />}
                                type="password"
                                placeholder="Пароль"
                                autoComplete='off'
                            />
                        </Form.Item>
                        <Form.Item>
                            <Button
                                loading={currentUserStore.loading}
                                type="primary"
                                htmlType="submit"
                            >
                                Войти
                            </Button>
                        </Form.Item>
                    </Form>
                </div>
            </div>
        </div>
        </div>
    );
});